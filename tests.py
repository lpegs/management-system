import pymysql

connection = pymysql.connect (host="localhost", user="root", password="123", database="management_system")

cursor = connection.cursor()

cursor.execute("select * from books")
connection.commit()

for i in cursor:
    print((i[0],i[1],i[2],i[3]))