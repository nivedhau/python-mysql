import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mypassword",
  database="myfavmovies"
)

mycursor = mydb.cursor()

sql = "INSERT INTO movies (name, actor, actress, releaseyear, director) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('ntep', 'jeeva', 'samantha', '2012', 'GVM'),
  ('ghajini', 'suriya', 'asin', '2005', 'ARM'),
  ('varanam-ayiram', 'suriya', 'sameera', '2008', 'GVM'),
  ('vtv', 'simbu', 'trisha', '2010', 'GVM')

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")