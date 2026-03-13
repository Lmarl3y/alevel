import bcrypt
import sqlite3
import random


# Database setup (sqlite)
conn = sqlite3.connect('ttt.db')
c = conn.cursor()
# Table for user creation//logging in
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
# Table for scores
c.execute('''CREATE TABLE IF NOT EXISTS scores
                (username TEXT PRIMARY KEY, wins INTEGER, losses INTEGER, draws INTEGER)''')
conn.commit()

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Encrypts password with bcrypt
    
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password)) # Sets up username and encrypted password into db
        c.execute("INSERT INTO scores (username, wins, losses, draws) VALUES (?, 0, 0, 0)", (username,)) # Sets up initial scores for user, starting at 0
        conn.commit()
        print("Registration successful")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.") # Username exists

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]): # Checks if password matches encryption & is in line with username
        print("Login Successful")
        return username
    else:
        print("Username or password is doesn't match database. Try again.")
        return None
    
def player_auth():
    # Register or login menu, returns username on success or None
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")
    while choice not in ['1', '2']:
        choice = input(f"{choice} isn't a valid option. Try again: ")
    if choice == '1':
        register()
        return login()  # log in after registering
    elif choice == '2':
        return login()

def menu():
    # Standard menu
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    menuchoice = input("Enter your choice: ") # gets user to enter 1-3
    while menuchoice not in ['1','2','3']:
        menuchoice = input(f"{menuchoice} isn't a valid option. Try again: ")
    if menuchoice == '1':
        register() # runs register function
    elif menuchoice == '2':
        username = login() # runs login function
        if username:
            pregame(username)
    elif menuchoice == '3':
        print("Exiting") # exits program, ending there.
        return

def pregame(player1):
    print("1. PVC") # PLay vs Computer
    print("2. PVP") # Play vs Player
    gamemode = input("Enter a choice:")
    while gamemode not in ['1', '2']:
        gamemode = input(f"{gamemode} isn't a valid option. Try again: ")
    if gamemode == '1':
        print("Starting PVC")
        pvc(player1)
    elif gamemode == '2':
        print(f"Player 1: {player1}")
        print("Player 2 - please register or login:")
        player2 = player_auth()
        if player2:
            print(f"Player 2: {player2}")
            pvp(player1, player2)
        else:
            print("Player 2 login failed.")

menu()

