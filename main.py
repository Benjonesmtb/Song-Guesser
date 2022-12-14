# Imports
import random
import sqlite3
import time
import datetime

def splitCSV():
    songs = []
    with open("TopSongs.csv") as f:
        ls = f.read().strip().split("\n")
    for i in range(len(ls)):
        songs.append(ls[i-1].split(","))
    return songs

def selectSong(songs):
    number = random.randint(0,len(songs)-1)
    print(number)
    selectedSong = songs[number]
    return selectedSong

def checkScore():
    db = sqlite3.connect('login.db')
    cursor = db.cursor()
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    row = cursor.fetchone()
    db.commit()
    db.close()
    return row[3]

def topFive():
    db = sqlite3.connect('login.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM users ORDER BY score ASC LIMIT 5''')
    for i in range(3):
        row = cursor.fetchone()
        print(row[1] , "-", row[3])
    db.commit()
    db.close()
    return row

def main(selectSong, splitCSV):
    songs = splitCSV()
    db = sqlite3.connect('login.db')
    cursor = db.cursor()
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    row = cursor.fetchone()
    db.close()
    if row is not None:
        print('Login successful!')
        guessCount = 0
        songToGuess = selectSong(songs)
        words = songToGuess[1].split(" ")
        start = datetime.datetime.now()
        while guessCount < 2:
            print("The first letter of the artist's name is:" , songToGuess[0][0])
            print("The first letter of each word in the songs title is:")
            for i in range(len(words)):
                print(words[i][0])
            guess = input("Enter the song name:").lower()
            if guess == songToGuess[1].lower():
                print("Correct")
                guessCount += 1
                db = sqlite3.connect("login.db")
                cursor = db.cursor()
                if guessCount == 1:
                    cursor.execute('''UPDATE users SET score = score+3 WHERE username = username;''')
                elif guessCount == 2:
                    cursor.execute('''UPDATE users SET score = score+3 WHERE username = username;''')
                db.commit()
                db.close()
                break
            else:
                print("Wrong")
                guessCount = guessCount + 1
        end = datetime.datetime.now()
        print("It took you:" , end - start , "to guess the song.")
    else:
        print('Incorrect username or password.')
    db = sqlite3.connect('login.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    row = cursor.fetchone()
    print("You have" , row[3] , "points.")
    db.commit()
    db.close()

# Menue System
while True:
    print("Welcome to a song guesser")
    print("Enter the number you select:")
    print("1 - Guess a song")
    print("2 - Check a Users Score")
    print("3 - Top 5 songs")
    print("4 - Exit")
    
    choice = input("Choice: ")
    if choice == '1':
        main(selectSong, splitCSV)

    elif choice == '2':
        print(checkScore())
    elif choice == '3':
        topFive()
    elif choice == '4':
        break
    else:
        print("Invalid please try again")
    print()
    time.sleep(1)