
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)


#cursor object

db_cursor=database.cursor()
#cursor execution
db_cursor.execute('CREATE DATABASE todoList')
print('success!')