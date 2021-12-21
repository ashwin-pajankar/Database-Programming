import pymysql

db = pymysql.connect(host="localhost",
                     user="root", password="test123",
                     database="sakila")

cursor = db.cursor()

sql = "DROP TABLE TEST_TABLE"

try:
    cursor.execute(sql)
    print("The table is dropped successfully!")
except:
    print("The object does not exist!")

db.close()






