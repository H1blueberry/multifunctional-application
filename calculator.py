def main():
    Task = True
    print("Type 'exit' to leave calculator")
    while True:
        task = input("Task: ")
        if task.lower() == "exit":
            break
        elif "*" in task:
            result = multiplication(task)
        elif "+" in task:
            result = addition(task)
        elif "/" in task:
            result = division(task)
        elif "-" in task:
            result = substraction(task)
        else:
            Task = False
        if Task == True:
            print(result)
        else:
            print("Sorry i don't undersatand that")
            print("Form: x*or/or+or-y")
            Task = True
    return


def multiplication(input):
    try:
        part1, part2 = input.split("*")
        part1_float = float(part1)
        part2_float = float(part2)
        return part1_float * part2_float
    except ValueError:
        print("Sorry I don't understand that")
        return ("Form: x*or/or+or-y")


def addition(task):
    try:
        part1, part2 = task.split("+")
        part1_float = float(part1)
        part2_float = float(part2)
        return part1_float + part2_float
    except ValueError:
        print("Sorry I don't understand that")
        return ("Form: x*or/or+or-y")


def division(task):
    try:
        part1, part2 = task.split("/")
        part1_float = float(part1)
        part2_float = float(part2)
        return part1_float / part2_float
    except ValueError:
        print("Sorry I don't understand that")
        return ("Form: x*or/or+or-y")


def substraction(task):
    try:
        part1, part2 = task.split("-")
        part1_float = float(part1)
        part2_float = float(part2)
        return part1_float - part2_float
    except ValueError:
        print("Sorry I don't understand that")
        return ("Form: x*or/or+or-y")


if __name__ == "__main__":
    main()
