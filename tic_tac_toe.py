import random
import sys
import time
import copy
sys.setrecursionlimit(1000)

def main():
    win = False
    full = []
    player1 = []
    player2 = []
    fields = ["upper_left", "upper_middle", "upper_right", "middle_left", "middle_middle", "middle_right", "bottom_left", "bottom_middle", "bottom_right"]
    fields2 = fields
    while (len(player1) + len(player2)) <= 9:
        if (len(player1) + len(player2)) < 9:
            print("Player1")
            field_pick = check_field(fields, player1, player2)
            player1.append(field_pick)
            fields2.remove(field_pick)
            draw_field(player1, player2)
            if check_win(player1) == True:
                end("player1")
                return
        if (len(player1) + len(player2)) < 9:
            print("Player2")
            field_pick = random_generate(fields2, player1, player2)
            player2.append(field_pick)
            fields2.remove(field_pick)
            draw_field(player1, player2)
            if check_win(player2) == True:
                end("player2")
                return
        if (len(player1) + len(player2)) == 9:
            print("It's a tie")
            sys.exit()


def check_field(fields, player1, player2):
    while True:
        field = input("Pick a field (form: upper/middle/bottom_left/middle/right): ")
        if field not in player1 and field not in player2 and field in fields:
            return field
        print(player1, player2, fields, field)


def random_generate(fields2, player, player2):
    if check_win(player) or check_win(player2) or (len(player)) + (len(player2)) == 9:
        return None
    board = copy.deepcopy(fields2)
    player_copy = copy.deepcopy(player)
    player2_copy = copy.deepcopy(player2)
    field, x = best_player2(board, player_copy, player2_copy)
    return field

def best_player(board, player, player2):
    if check_win(player) or check_win(player2) or (len(player)) + (len(player2)) == 9:
        return "a", utility(player, player2)
    v = 2
    for move in board:
        board2 = copy.deepcopy(board)
        board2.remove(move)
        player_2 = copy.deepcopy(player)
        player_2.append(move)
        x, v_other = best_player2(board2, player_2, player2)
        if v > v_other:
            v = v_other
            best = move
    return best, v


def best_player2(board, player, player2):
    if check_win(player) or check_win(player2) or (len(player)) + (len(player2)) == 9:
        return "a", utility(player, player2)
    v = -2
    for move in board:
        board2 = copy.deepcopy(board)
        board2.remove(move)
        player2_2 = copy.deepcopy(player2)
        player2_2.append(move)
        x, v_other = best_player(board2, player, player2_2)
        if v < v_other:
            v = v_other
            best = move
    return best, v


def utility(player, player2):
    if check_win(player):
        return -1
    elif check_win(player2):
        return 1
    else:
        return 0


def check_win(player):
    if "upper_left" in player and "upper_middle" in player and "upper_right" in player or "middle_left" in player and "middle_middle" in player and "middle_right" in player or "bottom_left" in player and "bottom_middle" in player and "bottom_right" in player or "upper_left" in player and "middle_middle" in player and "bottom_right" in player or "upper_right" in player and "middle_middle" in player and "bottom_left" in player or "upper_left" in player and "middle_left" in player and "bottom_left" in player or "upper_middle" in player and "middle_middle" in player and "bottom_middle" in player or "upper_right" in player and "middle_right" in player and "bottom_right" in player:
        return True
    return False


def draw_field(player1, player2):
    print(" ")
    if "upper_left" not in player1 and "upper_left" not in player2:
        print("   |",end ="")
    elif "upper_left" in player1:
        print(" X |",end ="")
    elif "upper_left" in player2:
        print(" O |",end ="")

    if "upper_middle" not in player1 and "upper_middle" not in player2:
        print("   |",end ="")
    elif "upper_middle" in player1:
        print(" X |", end = "")
    elif "upper_middle" in player2:
        print(" O |", end = "")

    if "upper_right" not in player1 and "upper_right" not in player2:
        print("   ")
    elif "upper_right" in player1:
        print(" X ")
    elif "upper_right" in player2:
        print(" O ")

    if "middle_left" not in player1 and "middle_left" not in player2:
        print("   |",end = "")
    elif "middle_left" in player1:
        print(" X |",end = "")
    elif "middle_left" in player2:
        print(" O |",end = "")

    if "middle_middle" not in player1 and "middle_middle" not in player2:
        print("   |",end  ="")

    elif "middle_middle" in player1:
        print(" X |",end ="")
    elif "middle_middle" in player2:
        print(" O |",end ="")

    if "middle_right" not in player1 and "middle_right" not in player2:
        print("   ")
    elif "middle_right" in player1:
        print(" X ")
    elif "middle_right" in player2:
        print(" O ")

    if "bottom_left" not in player1 and "bottom_left" not in player2:
        print("   |",end ="")
    elif "bottom_left" in player1:
        print(" X |",end ="")
    elif "bottom_left" in player2:
        print(" O |",end ="")

    if "bottom_middle" not in player1 and "bottom_middle" not in player2:
        print("   |",end ="")
    elif "bottom_middle" in player1:
        print(" X |",end ="")
    elif "bottom_middle" in player2:
        print(" O |",end ="")

    if "bottom_right" not in player1 and "bottom_right" not in player2:
        print("   ")
    elif "bottom_right" in player1:
        print(" X ")
    elif "bottom_right" in player2:
        print(" O ")

    print("")
    return


def end(winner):
    if winner == "player1":
        print("You are the winner")
    else:
        print("You lost")
    return


if __name__ == "__main__":
    main()
