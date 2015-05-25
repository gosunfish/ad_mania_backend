from config import Config
import logging
import xml.etree.ElementTree as ET
from mysql.connector import MySQLConnection, Error
import requests
from codecs import encode
from lxml import html

logger = logging.getLogger(__name__)

def shred_result(result_xml):
    result_dict = dict()
    root = ET.fromstring(result_xml)
    result_dict['records_returned'] = root.find('links').get('records-returned')
    return result_dict

def database_update():

    logger.debug('Database Update Starting')
    config=Config()
    user = config['DB_LOGIN']
    password = config['DB_PW']
    host = config['DB_HOST']
    database = config['DB_NAME']
    cjauth = config['CJ_AUTH']
    cjurl = config['CJ_URL']

    conn = MySQLConnection(user=user, password=password, host=host, database=database)
    conn.autocommit = True
    cursor = conn.cursor()

    page_number = 0
    total_records_returned = 0
    records_per_page = 100 # this is the max number allowed by the affiliate api per call.
    records_returned = records_per_page
    headers = {'authorization': cjauth}

    while records_returned == records_per_page:
        page_number += 1
        params = {'website-id': '7782886', 'link-type': 'banner', 'advertiser-ids': 'joined', 'page-number': page_number, 'records-per-page': records_per_page}

        result = requests.get(cjurl, headers=headers, params=params)
        result_xml = result.text

        root = ET.fromstring(result_xml.encode('utf8'))
        records_returned = int(root.find('links').get('records-returned'))
        total_matched = int(root.find('links').get('total-matched'))
        total_records_returned += records_returned

        logger.info('Total Matched: {}, Records Returned: {}, Total Records Returned: {}'.format(total_matched, records_returned, total_records_returned))

        link_number = 0
        for link in root.iter('link'):
            link_number+= 1
            percent_complete = ((total_records_returned - records_returned + link_number) * 100) / total_matched
            logger.debug('Page Number: {}, Link Number: {}, Percent Complete: {}%'.format(page_number, link_number, percent_complete))
            link_code_html = html.fromstring(link.find('link-code-html').text)
            height = int(link_code_html.xpath('//img/@height')[0])
            width = int(link_code_html.xpath('//img/@height')[0])

            mysql_args = (
                link.find('link-id').text,
                link.find('advertiser-id').text,
                link.find('advertiser-name').text,
                link.find('category').text,
                'None' if link.find('promotion-start-date').text == None else link.find('promotion-start-date').text,
                'None' if link.find('promotion-end-date').text == None else link.find('promotion-end-date').text,
                height,
                width,
                link.find('link-code-html').text.replace('7782886', '##DOMAIN_ID##'))

            try:
                cursor.callproc('AdMania.prc_UpdateAd',mysql_args)

            except Error as e:
                print e

    cursor.close()
    conn.close()

    logger.debug('Database Update Complete')


if __name__ == '__main__':
    database_update()


# http://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html