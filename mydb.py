import mysql.connector

#Create data base connection
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'rootpassword',
	)
	
#Create a  middleware between SQLite database connection and SQL query 
#(Cursor Object)

cursorObject = dataBase.cursor()

#Create the database itselfS
cursorObject.execute("CREATE DATABASE 3340data")
print("Hello data base 3340data")