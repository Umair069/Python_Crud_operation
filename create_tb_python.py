import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="umair")

mycursor = mydb.cursor()

# mycursor.execute("Create table employee (name varchar(200), salary int(20))")

mycursor.execute("Show tables")

for db in mycursor:
    print(db)
