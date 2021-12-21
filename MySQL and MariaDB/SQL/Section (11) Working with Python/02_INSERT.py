import pymysql

db = pymysql.connect(host="localhost",
                     user="root", password="test123",
                     database="sakila")

cursor = db.cursor()

sql1 = """INSERT INTO TEST_TABLE (FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES('Ashwin', 'Pajankar', 35, 'M', 10000)"""

sql2 = """INSERT INTO TEST_TABLE (FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES('Thor', 'Odinson', 35, 'M', 2000)"""

sql3 = """INSERT INTO TEST_TABLE (FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES('Tony', 'Stark', 45, 'M', 40000)"""

sql4 = """INSERT INTO TEST_TABLE (FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES('Jane', 'Foster', 32, 'F', 3000)"""

sqls = [sql1, sql2, sql3, sql4]

try:
    for query in sqls:
        cursor.execute(query)
        db.commit()
    print("The records are inserted successfully!")
except:
    print("The records were not inserted successfully!")

db.close()






