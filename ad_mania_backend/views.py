from ad_mania import app
from flask import url_for, redirect, render_template, request, jsonify
from mysql.connector import MySQLConnection, Error
import json
import logging

logger = logging.getLogger(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('ads'))


@app.route('/ads', methods=['GET'])
def ads():
    website = request.args.get('website')
    user = app.config['DB_LOGIN']
    password = app.config['DB_PW']
    host = app.config['DB_HOST']
    database = app.config['DB_NAME']

    conn = MySQLConnection(user=user, password=password, host=host, database=database)
    cursor = conn.cursor()
    cursor.callproc('AdMania.prc_GetAds',website)
    result_set = []
    row = cursor.fetchone()
    while row:
        result_set.append(row)

    return render_template('T1.html',resultsSET=result_set)



