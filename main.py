import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mypassword",
  database="myfavmovies"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM movies")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("**************************")

mycursor1 = mydb.cursor()

sql1 = "SELECT name FROM movies WHERE actor='suriya'"

mycursor1.execute(sql1)

myresult1 = mycursor1.fetchall()

for x in myresult1:
  print(x)