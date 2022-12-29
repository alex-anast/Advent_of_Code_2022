"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you.
"Anyway, the second column says how the round needs to end: X means you need to lose,
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out
what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y),
so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
according to your strategy guide?
"""


def Who_Won(p1_num, p2_num) -> int:
    if p1_num == 1:
        if p2_num == 1:
            return 3
        elif p2_num == 2:
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


def Map_Answer(answer) -> int:
    if answer == "A":
        return 1
    elif answer == "B":
        return 2
    elif answer == "C":
        return 3


def Strategy(answer, first_input) -> int:
    if answer == "X":
        # LOSE
        temp_list = [1, 2, 3]
        for i in temp_list:
            if (first_input) == i:
                return int(temp_list[(i + 1) % 3])
    elif answer == "Y":
        # DRAW
        return first_input
    elif answer == "Z":
        # WIN   - result will always be behind
        temp_list = [1, 2, 3]
        for i in temp_list:
            if (first_input) == i:
                return int(temp_list[i % 3])


game_eq = ["Rock", "Paper", "Scissors"]

with open(
    "/home/alex_anast/workspace/advent_of_code_2022/day2/data_input", mode="r"
) as my_file:
    contents = my_file.readlines()

player1_total = 0
player2_total = 0

for turn in contents:
    player_letter = []
    [player_letter.append(letter) for letter in turn.split()]

    print(player_letter)

    player1 = Map_Answer(player_letter[0])
    player2 = Strategy(player_letter[1], player1)
    print(f" = {player1} vs {player2} = ")

    result = Who_Won(player1, player2)

    if result == 6:
        player1 = player1 + result
    elif result == 3:
        player1 = player1 + result
        player2 = player2 + result
    else:
        player2 = player2 + abs(6 - result)

    player1_total = player1_total + player1
    player2_total = player2_total + player2
    print(f"P1\t{player1_total}\tvs\t{player2_total}\tP2")
