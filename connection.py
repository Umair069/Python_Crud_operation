import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="")

print(mydb)

if(mydb):
    print("Connection Successfull")
else:
    print("Connection Unsucessfull")