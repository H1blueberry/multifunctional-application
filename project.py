import todo
import Blackjack
import tic_tac_toe
import calculator
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import time
import sys
import random
from tabulate import tabulate

db = SQL("sqlite:///users.db")
id = None
activities = [["Play Tic tac Toe"], ["Play Blackjack"], ["Calculator"], ["Enter entry to Todo list"], ["see Todo list"], ["Delete entry from Todo list"]]
header = ["Activities"]


def main():
    start()
    greeting()
    program()
    print("done")


def greeting():
    print("---------------------------------------------------------------")
    print("                                                               ")
    print("---------------------------------------------------------------")
    name = db.execute("SELECT username FROM users WHERE id = ?", id)
    name = name[0]["username"]
    patterns_greeting = ["Hi how are you?", f"Hi {name}", f"Nice to see you {name}", f"Hi {name}, how are you doing?"]
    patterns_greeting2 = ["Is there anything I can do for you?", "What do you want to do?", "How can I help you today?"]
    print(random.choice(patterns_greeting))
    print("\n")
    time.sleep(1)
    print(random.choice(patterns_greeting2))
    print("These are the things you can do: ")
    print(tabulate(activities, header, tablefmt="grid"))
    print("Press 'quit' to quit the program")
    return



def start():
    while True:
        print("\n")
        print("---------------------------------------------------------------")
        print("                                                               ")
        print("---------------------------------------------------------------")
        print("\n")
        start = input("Press 'l' to login an 'r' to register: ")
        if start == "l":
            if login() == True:
                break
        elif start == "r":
            if register() == True:
                pass
        else:
            pass
    return


def login():
    print("\n")
    print("---------------------------------------------------------------")
    print("                          Login                                ")
    print("---------------------------------------------------------------")
    print("\n")
    username = input("Username: ")
    password = input("Password: ")
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)
    if len(rows) != 1:
        print("Invalid password and/or username")
        time.sleep(0.5)
        return False
    password_hash = db.execute("SELECT hash FROM users WHERE username = ?", username)
    if not check_password_hash(password_hash[0]["hash"], password):
        print("Invalid password and/or username")
        time.sleep(0.5)
        return False
    global id
    id = db.execute("SELECT id FROM users WHERE username = ?", username)
    id = id[0]["id"]
    print("\n")
    print("Succesfully loged in")
    time.sleep(0.5)
    print("\n")
    return True


def register():
    print("\n")
    print("---------------------------------------------------------------")
    print("                         Register                              ")
    print("---------------------------------------------------------------")
    print("\n")
    username = input("Username: ")
    password = input("password: ")
    confirmation = input("Confirm your password: ")
    if username != (""):
        t = db.execute('SELECT * FROM users WHERE username = ?', username)
        if len(t) != 0:
            print("Username already exists!")
            time.sleep(0.5)
            return False
        elif password == (""):
            print("Must enter a password!")
            time.sleep(0.5)
            return False
        elif confirmation == (""):
           print("Must enter a confirmation!")
           time.sleep(0.5)
           return False
        elif confirmation != password:
            print("Password and confirmation are not equal!")
            time.sleep(0.5)
            return False
        else:
            print("\n")
            print("Succesfully registered!")
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            time.sleep(0.4)
            print("\n")
            return True
    else:
        print("Must enter a username!")
        time.sleep(0.5)
        return False

def program():
    while True:
        request = input("")
        if request.lower() == "quit":
            sys.exit()
        print("\n")
        print("---------------------------------------------------------------")
        print("                                                               ")
        print("---------------------------------------------------------------")
        if "tic" in request.lower():
            tic_tac_toe.main()
            time.sleep(2)
        elif "blackjack" in request.lower():
            Blackjack.main()
            time.sleep(2)
        elif "calculat" in request.lower():
            calculator.main()
        elif "enter" in request.lower():
            todo.enter(id)
        elif "see" in request.lower():
            todo.see(id)
        elif "delete" in request.lower():
            todo.delete(id)
        else:
            print("Sorry I don't understand that")
        print("---------------------------------------------------------------")
        print("                                                               ")
        print("---------------------------------------------------------------")
        print("\n")
        print(tabulate(activities, header, tablefmt="grid"))

if __name__ == "__main__":
    main()
