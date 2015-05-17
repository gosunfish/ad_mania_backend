from config import Config
from mysql.connector import MySQLConnection, Error


config=Config().config
user = config['DB_LOGIN']
password = config['DB_PW']
host = config['DB_HOST']
database = config['DB_NAME']


conn = MySQLConnection(user=user, password=password, host=host, database=database)
conn.autocommit = True
cursor = conn.cursor()

args = (1111,2222,'2015-06-06','2015-06-07','HHHTTTMMMLLO')
cursor.callproc("prc_UpdateAd", args)
cursor.execute("select * from Ad;")
rows = cursor.fetchall()
for row in rows:
    print row[0],row[1]

cursor.close()
conn.close()
