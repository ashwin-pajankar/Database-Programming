import pymysql

db = pymysql.connect(host="localhost",
                     user="root", password="test123",
                     database="sakila")

cursor = db.cursor()

sql = "SELECT VERSION()"

cursor.execute(sql)

data = cursor.fetchone()

print("Database Version : %s" % data)

db.close()






