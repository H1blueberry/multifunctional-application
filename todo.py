from cs50 import SQL
from tabulate import tabulate

db = SQL("sqlite:///users.db")


def see(id):
    print("                     your Todo list                            ")
    entry = db.execute("SELECT entry FROM Todo WHERE user_id = ?", id)
    number = db.execute("SELECT id FROM Todo WHERE user_id = ?", id)
    for i in range (len(entry)):
        entry[i] = [entry[i]["entry"]]
        entry[i].append(number[i]["id"])
    head = ["Entry", "Number"]
    print("\n")
    print(tabulate(entry, head, tablefmt="grid"))
    print("\n")
    print("Press 'exit' to leave")
    print("\n")
    exit = input()
    if exit.lower() == "exit":
        return


def enter(id):
    entry = input("Add something to your Todo list: ")
    db.execute("INSERT INTO Todo (user_id, entry) VALUES (?, ?)", id, entry)
    print("\n")
    see(id)


def delete(id):
    entry = db.execute("SELECT entry FROM Todo WHERE user_id = ?", id)
    number = db.execute("SELECT id FROM Todo WHERE user_id = ?", id)
    for i in range (len(entry)):
        entry[i] = [entry[i]["entry"]]
        entry[i].append(number[i]["id"])
    head = ["Entry", "Number"]
    print("\n")
    print(tabulate(entry, head, tablefmt="grid"))
    print("\n")
    remove = input("Enter the number of the entry you want to delete: ")
    db.execute("DELETE FROM Todo WHERE id = ? AND user_id = ? ", remove, id)
    print("\n")
    see(id)
