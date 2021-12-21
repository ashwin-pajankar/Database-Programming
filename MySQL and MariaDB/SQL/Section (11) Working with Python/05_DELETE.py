import pymysql

db = pymysql.connect(host="localhost",
                     user="root", password="test123",
                     database="sakila")

cursor = db.cursor()

sql = "DELETE FROM TEST_TABLE"

try:
    cursor.execute(sql)

    db.commit()
    print("The records are deleted successfully!")
except:
    db.rollback()
    print("The records were not deleted successfully!")

db.close()






