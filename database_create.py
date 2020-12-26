import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="")

mycursor = mydb.cursor()

mycursor.execute("Show Databases")

for db in mycursor:
    print(db)