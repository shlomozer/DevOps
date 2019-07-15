# Establishing a connection to DB
import pymysql as pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Aa123456', db='Users')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM users.players;")

# Iterating table and printing all users
for row in cursor:
    print(row)

#cursor.execute("INSERT INTO users.players(id,name)VALUES(2,'shay');")
conn.commit()

#cursor.execute("DELETE FROM users.players WHERE name='shay'")
conn.commit()

#cursor.execute("UPDATE users.players SET id='10' WHERE name='shay'")
conn.commit()

cursor.close()
conn.close()



