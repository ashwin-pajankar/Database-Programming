import pymysql

db = pymysql.connect(host="localhost",
                     user="root", password="test123",
                     database="sakila")

cursor = db.cursor()

sql = "SELECT * FROM TEST_TABLE"

try:
    cursor.execute(sql)

    resultset = cursor.fetchall()

    for row in resultset:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]

        print("%s %s, %d, %s, %d" %
              (fname, lname, age, sex, income))

    print("The records are fetched successfully!")
except:
    print("The records were not fetched successfully!")

db.close()






