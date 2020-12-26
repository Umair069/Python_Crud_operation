import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="umair")

mycursor = mydb.cursor()

mycursor.execute("Select * from employee")

myresult=mycursor.fetchall()
'''fatchmany constains 1 row 
fetchone cotains 1 coloumns 
fetchall contains all table
'''

for row in myresult:
    print(row)