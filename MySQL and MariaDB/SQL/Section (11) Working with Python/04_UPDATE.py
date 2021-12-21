import pymysql

db = pymysql.connect(host="localhost",
                     user="root", password="test123",
                     database="sakila")

cursor = db.cursor()

sql = "UPDATE TEST_TABLE SET INCOME = INCOME + 500"

try:
    cursor.execute(sql)

    db.commit()
    print("The records are updated successfully!")
except:
    db.rollback()
    print("The records were not updated successfully!")

db.close()






