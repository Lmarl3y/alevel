import sqlite3
import random

# ---------------- DATABASE SETUP ----------------

conn = sqlite3.connect("tictactoe.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores(
    player_name TEXT,
    score INTEGER
)
""")

conn.commit()

# ---------------- AUTHENTICATION ----------------

def login_player(player_num):

    print(f"\nPlayer {player_num} Login")

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute("SELECT * FROM players WHERE username=? AND password=?",
                   (username, password))

    result = cursor.fetchone()

    if result:
        print("Login successful")
        return username
    else:
        print("User not found. Creating new account.")
        cursor.execute("INSERT INTO players VALUES (?,?)", (username, password))
        conn.commit()
        return username


# ---------------- BOARD ----------------

board = [[" " for x in range(3)] for y in range(3)]


def display_board():
    print("\n")
    for row in board:
        print(row[0] + " | " + row[1] + " | " + row[2])
        print("--+---+--")
    print("\n")


# ---------------- MOVE FUNCTIONS ----------------

def player_move(symbol):

    while True:

        try:
            row = int(input("Row (0-2): "))
            col = int(input("Col (0-2): "))

            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid position")
                continue

            if board[row][col] != " ":
                print("Space already taken")
                continue

            board[row][col] = symbol
            break

        except:
            print("Invalid input")


def computer_move():

    empty = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                empty.append((r,c))

    move = random.choice(empty)
    board[move[0]][move[1]] = "O"

    print("Computer placed O")


# ---------------- WIN CHECK ----------------

def check_winner(symbol):

    # rows
    for row in board:
        if row.count(symbol) == 3:
            return True

    # columns
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True

    # diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False


# ---------------- DRAW CHECK ----------------

def check_draw():

    for row in board:
        if " " in row:
            return False

    return True


# ---------------- SAVE SCORE ----------------

def save_score(player):

    cursor.execute(
        "INSERT INTO scores VALUES (?,1)",
        (player,)
    )

    conn.commit()


# ---------------- SHOW TOP 5 ----------------

def show_top_scores():

    print("\nTop 5 Scores\n")

    cursor.execute("""
    SELECT player_name, SUM(score) as total
    FROM scores
    GROUP BY player_name
    ORDER BY total DESC
    LIMIT 5
    """)

    results = cursor.fetchall()

    for r in results:
        print(r[0], "-", r[1])


# ---------------- GAME ----------------

print("TIC TAC TOE\n")

player1 = login_player(1)

mode = input("Play vs computer? (y/n): ")

if mode.lower() == "y":
    player2 = "Computer"
else:
    player2 = login_player(2)

display_board()

while True:

    print(player1 + "'s turn (X)")
    player_move("X")
    display_board()

    if check_winner("X"):
        print(player1, "wins!")
        save_score(player1)
        break

    if check_draw():
        print("Game Draw")
        break

    if player2 == "Computer":
        computer_move()
    else:
        print(player2 + "'s turn (O)")
        player_move("O")

    display_board()

    if check_winner("O"):
        print(player2, "wins!")
        save_score(player2)
        break

    if check_draw():
        print("Game Draw")
        break


show_top_scores()

conn.close()
