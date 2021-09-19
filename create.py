import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mypassword",
  database="myfavmovies"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE movies (name VARCHAR(255),actor VARCHAR(255), actress VARCHAR(255), releaseyear VARCHAR(255), director VARCHAR(255))")