import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="8547",database="projects1")
mycursor=mydb.cursor()
mycursor.execute("select * from datas")
for i in mycursor:
    print(i)