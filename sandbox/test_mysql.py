
import mysql.connector

conn = mysql.connector.connect(user='admin', password='aDmaniA1',host='web-sites.cqnknvzsrvqd.us-east-1.rds.amazonaws.com',database='AdMania')

cursor = conn.cursor()

query = ("SHOW TABLES;")

cursor.execute(query)

for row in cursor:
  print row

query = ("DESCRIBE Ad;")

cursor.execute(query)

for row in cursor:
  print row

cursor.close()
conn.close()

