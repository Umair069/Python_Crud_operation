import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="umair")

mycursor = mydb.cursor()

sqlform = "Insert into employee(name,salary) values(%s,%s)"

employee = [("Umair",200000),("Rafay",300000),("hassnain",400000)]

mycursor.executemany(sqlform,employee)

mydb.commit()
