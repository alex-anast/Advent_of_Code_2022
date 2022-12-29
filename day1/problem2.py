"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf
carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories
carried by the top three Elves carrying the most Calories. That way, even if one of those Elves
runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories),
then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories).
The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


def Sum_Calories_per_Elf(contents) -> list:
    calories_per_elf = []
    elf = 0
    for food in contents:
        if food != "\n":
            elf = elf + int(food)
        else:
            calories_per_elf.append(elf)
            elf = 0
    return calories_per_elf


with open("/home/user/workspace/99_my_workspace/data_input", mode="r") as my_file:
    contents = my_file.readlines()

calories_top_3 = Sum_Calories_per_Elf(contents)
calories_top_3.sort()
calories_top_3.reverse()
print(sum(calories_top_3[:3]))
