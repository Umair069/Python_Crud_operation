import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="umair")

mycursor = mydb.cursor()

sql = "UPDATE employee SET salary=700000 where name='Umair'"

mycursor.execute(sql)

mydb.commit()
