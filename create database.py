import mysql.connector
mysdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123'
)
mycursor=mysdb.cursor()
mycursor.execute('CREATE DATABASE ajay')
print('success')
mysdb.close()




