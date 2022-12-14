# Import the necessary modules
import sqlite3

# Connect to the database
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# Prompt the user to enter their login information
username = input('Enter your username: ')
password = input('Enter your password: ')

# Check the database to see if the entered username and password are correct
cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))

# Allow the user access to the system if their login information is correct
if cursor.fetchone() is not None:
    print('Login successful!')
else:
    print('Incorrect username or password.')

# Close the database connection
conn.close()
