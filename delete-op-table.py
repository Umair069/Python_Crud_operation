import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="umair")

mycursor = mydb.cursor()

mydel = "DELETE from employee where name='Umair'"

mycursor.execute(mydel)

mydb.commit()

