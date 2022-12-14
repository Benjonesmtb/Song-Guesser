import sqlite3

# create a connection to the database
db = sqlite3.connect('login.db')
cursor = db.cursor()




cursor.execute('''SELECT * FROM users ORDER BY score DESC LIMIT 5''')
for i in range(3):
    row = cursor.fetchone()
    print(row[1] , "-", row[3])
#db.commit()
db.close()