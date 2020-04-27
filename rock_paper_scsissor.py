import random

moves = {"rock": 1, "paper": 2, "scissor": 3}
move_name = ["rock", "paper", "scissor"]

def player():
    move = input("Enter your move: ")
    if move in moves:
        print(int(moves[move]))
        return int(moves[move])
    else:
        print("INVALID MOVE!")
        player()


def com():
    move = int(random.uniform(1, 3))
    print(move)
    return move


def compair(player, com):
    print(f"player: {move_name[player-1]}\ncomputer: {move_name[com-1]}")
    if (player == 1 and com == 3) or (player == 2 and com == 1) or (player == 3 and com == 2):
        return "player"
    elif (player == 1 and com == 2) or (player == 2 and com == 3) or (player == 3 and com == 1):
        return "com"
    elif player == com:
        return 'tie'
    else:
        return 'error'


win = 0
lose = 0
tie = 0

while 1:
    print(f"Number of wins: {win}\nnumber of loses: {lose}\nnumber of ties: {tie}\n")
    command = input("1: to play\n2: to reset score\nchoice: ")
    if command == '1':
        winner = compair(player(), com())
        print(winner)
        if winner == 'player':
            win += 1
        elif winner == 'com':
            lose += 1
        else:
            tie += 1
    elif command == 2:
        lose = 0
        win = 0
        tie = 0
    else:
        print("INVALID INPUT")
