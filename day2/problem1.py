"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage,
a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds;
in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape.
Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they
say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get
if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8
(2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""

from random import randint


# Fucktard, that's not how you should approach the problem..
def Make_Choice() -> dict:
    # choice = randint(1,3)
    choice = input("Choose a number [ 1 / 2 / 3 ]\n")
    return int(choice)


def Who_Won(p1_num, p2_num) -> int:
    # p1_num = int([p1_num[i] for i in p1_num])
    # p2_num = int([p2_num[i] for i in p2_num])
    # print(f"{p1_num} vs {p2_num}")
    if p1_num == 1:
        if p2_num == 1:
            # if draw : 3 points
            return 3
        elif p2_num == 2:
            # if lost : 0 points
            return 0
        else:
            return 6
    elif p1_num == 2:
        if p2_num == 1:
            return 6
        elif p2_num == 2:
            return 3
        else:
            return 0
    else:
        if p2_num == 1:
            return 0
        elif p2_num == 2:
            return 6
        else:
            return 3


def Map_Answer(player_answer) -> int:
    for answer in player_answer:
        if answer == "A" or answer == "X":
            return 1
        elif answer == "B" or answer == "Y":
            return 2
        elif answer == "C" or answer == "Z":
            return 3
        else:
            assert False


game_eq = ["Rock", "Paper", "Scissors"]


with open(
    "/home/alex_anast/workspace/advent_of_code_2022/day2/data_input", mode="r"
) as my_file:
    contents = my_file.readlines()

player1_total = 0
player2_total = 0

# At first I had understood the problem completely differently
# In the end, it is very very much simpler...
for turn in contents:
    # print(turn)

    # player1 = Make_Choice()
    # player2 = Make_Choice()

    player_answer = []
    [player_answer.append(Map_Answer(letter)) for letter in turn.split()]

    player1 = player_answer[0]
    player2 = player_answer[1]

    # returns the winner and his total points in a single content dictionary
    result = Who_Won(player1, player2)
    # print(f"Result is ... {result}")
    # if result == 3 :
    #     print("draw")
    # elif result == 6:
    #     print("Player 1 won!")
    # elif result == 0:
    #     print("Player 2 won!")
    # else:
    #     print("FUCKED UP")

    # assert(isinstance(player1, int))

    # print("===== ===== RESULT ===== =====")
    # print(f"P1\t{game_eq[player1-1]}\tvs\t{game_eq[player2-1]}\tP2")
    player1 = player1 + result
    player2 = player2 + abs(6 - result)
    # print(f"P1\t{player1}\tvs\t{player2}\t\tP2")

    player1_total = player1_total + player1
    player2_total = player2_total + player2
    print(f"P1\t{player1_total}\tvs\t{player2_total}\tP2")
