import random


def main():
    game_over = True

    score = 0
    score_computer = 0
    aktueller_wurf = 0
    aktueller_wurf_computer = 0
    karten = [1, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, "Bube", "Dame", "König", "As"]
    karten2 = [10, "Bube", "Dame", "König"]
    start = input("Press 'y' to start the game? ")

    if  start.lower() == "y":
        game_over = False

    while game_over == False:
            aktueller_wurf = random.randint(2,11)
            aktueller_wurf_computer = random.randint(2,11)
            if (aktueller_wurf == 10):
                print("Your card: ")
                print(random.choice(karten2))
                if ((random.choice(karten2)) == 10):
                    print("Your card: ")
                    print("...........")
                    print("../| |   |.")
                    print("./ | |   |.")
                    print("/  | |   |.")
                    print("   | |___|.")
                    print("...........")
                if ((random.choice(karten2)) == "Bube"):
                    print("...........")
                    print("..._____...")
                    print("..|     |..")
                    print("..| ----|..")
                    print("..| ----|..")
                    print("..|_____|..")
                    print("...........")
                if ((random.choice(karten2)) == "Dame"):
                    print("...........")
                    print("..._____...")
                    print("..|     \..")
                    print("..|     |..")
                    print("..|     |..")
                    print("..|_____/..")
                    print("...........")
                if ((random.choice(karten2)) == "König"):
                    print("...........")
                    print(".|  /    ..")
                    print(".| /     ..")
                    print(".|/      ..")
                    print(".|\      ..")
                    print(".| \     ..")
                    print(".|  \    ..")
                    print("...........")
            else:
                if (aktueller_wurf == 11):
                    print("Your card: ")
                    print("...........")
                    print("..../ \....")
                    print(".../   \...")
                    print("../-----\..")
                    print("./       \.")
                    print("...........")
                else:
                    print("Your card:")
                    if (aktueller_wurf == 2):
                        print("............")
                        print("..________..")
                        print("..........|.")
                        print("..........|.")
                        print("..________|.")
                        print("..|.........")
                        print("..|.........")
                        print("..|_______..")
                        print("............")
                    if (aktueller_wurf == 3):
                        print("............")
                        print(".__________.")
                        print(".         |.")
                        print(".         |.")
                        print("._________|.")
                        print(".         |.")
                        print(".         |.")
                        print("._________|.")
                        print("............")
                    if (aktueller_wurf == 4):
                        print("............")
                        print(".|         .")
                        print(".|         .")
                        print(".|         .")
                        print(".|____|____.")
                        print(".     |    .")
                        print("............")
                    if (aktueller_wurf == 5):
                        print("............")
                        print(".__________.")
                        print(".|         .")
                        print(".|         .")
                        print(".|_________.")
                        print(".         |.")
                        print(".         |.")
                        print("._________|.")
                    if (aktueller_wurf == 6):
                        print("............")
                        print(".__________.")
                        print(".|         .")
                        print(".|         .")
                        print(".|_________.")
                        print(".|        |.")
                        print(".|        |.")
                        print(".|________|.")
                        print("............")
                    if (aktueller_wurf == 7):
                        print(".............")
                        print("._________...")
                        print(".        |...")
                        print(".        |...")
                        print(".  ______|__.")
                        print(".        |...")
                        print(".        |...")
                        print(".............")
                    if (aktueller_wurf == 8):
                        print("............")
                        print(".__________.")
                        print(".|        |.")
                        print(".|        |.")
                        print(".|________|.")
                        print(".|        |.")
                        print(".|        |.")
                        print(".|________|.")
                        print("............")
                    if (aktueller_wurf == 9):
                        print("............")
                        print(".__________.")
                        print(".|        |.")
                        print(".|        |.")
                        print(".|________|.")
                        print(".         |.")
                        print(".         |.")
                        print("._________|.")
                        print("........... ")
            score += aktueller_wurf
            score_computer += aktueller_wurf_computer
            print("Sum of all your cards:")
            print(score)
            if score > 21:
                print("The sum of al your cards is more than 21. You lost")
                game_over = True
            else:
                if score_computer > 21:
                    print("The sum of my cards is more than 21. I lost")
                    game_over = True
                else:
                    spiel = input("Press 'y' if you want to continue playing? ")
                    if spiel.lower() == 'y':
                        game_over = False
                    else:
                        game_over = True
                        if score > score_computer:
                            print("You are the winner")
                        if score < score_computer:
                            print("You lost")
                        if score == score_computer:
                            print("It's tie")
                        print("sum of oyur cards: ")
                        print(score)
                        print("Sum of my cards: ")
                        print(score_computer)
                        game_over = True


if __name__ == "__main__":
    main()
