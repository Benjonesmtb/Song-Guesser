# Import the necessary module
import sqlite3


def create():
# Connect to the database
  conn = sqlite3.connect('login.db')
  cursor = conn.cursor()

# Create the "users" table
  cursor.execute('CREATE TABLE users (id TEXT, username TEXT, password TEXT, score NUMBER)')

# Add some users to the database
  cursor.execute('INSERT INTO users VALUES ("1", "johndoe", "secret", 1)')
  cursor.execute('INSERT INTO users VALUES ("2", "janedoe", "password", 2)')
  cursor.execute('INSERT INTO users VALUES ("3", "user1", "pass1", 36)')
  cursor.execute('INSERT INTO users VALUES ("4", "user2", "pass2", 4)')
  cursor.execute('INSERT INTO users VALUES ("5", "user3", "pass3", 8)')
  cursor.execute('INSERT INTO users VALUES ("6", "user4", "pass4", 2)')
  print(1)

# Save the changes
  conn.commit()

# Close the database connection
  conn.close()
  print(2)

def clear():
  conn = sqlite3.connect('login.db')
  cursor = conn.cursor()

# Clear the database
  cursor.execute('DELETE FROM users')

# Save the changes
  conn.commit()

# Close the database connection
  conn.close()

create()
