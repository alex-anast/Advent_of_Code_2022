"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey.  Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.  Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments.  The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.  The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).  The list of items for each rucksack is given as characters all on a single line.  A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.  For example, suppose you have the following list of contents from six rucksacks: vJrwpWtwJgWrhcsFMMfFFhFp jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL PmmdzqPrVvPwwTWBwg wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn ttgJtRGJQctTZtZT CrZsJsPPZsGzwwsLwLmpwMDw The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.  The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.  The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.  The fourth rucksack's compartments only share item type v.  The fifth rucksack's compartments only share item type t.  The sixth rucksack's compartments only share item type s.  To help prioritize item rearrangement, every item type can be converted to a priority: Lowercase item types a through z have priorities 1 through 26.  Uppercase item types A through Z have priorities 27 through 52.  In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.  Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types? 
"""

print("Here we go!")

"""
two compartments
one item type WRONG per compartment
'a' != 'A'
same num of items (not types!) in each compartment

6 Rucksacks: 

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

each line is a rucksack
left half is one compartment, right half is the other compartment
some chars (item types) appear in both compartments. That's how you find which is wrong. There can only be 1 wrong.

"""


def findWrong(c1, c2) -> str:
    for item_type_1 in c1:
        for item_type_2 in c2:
            if item_type_1 == item_type_2:
                # print(item_type_1, item_type_2)
                # print(type(item_type_1))
                return item_type_1


hash_table = {}

for i in range(52):
    """
    'A' => 65
    'Z' => 90
    ...
    'a' => 97
    'z' => 122
    """
    if i <= 25:
        hash_table[chr(65 + i).lower()] = i + 1
    else:
        hash_table[chr(71 + i).upper()] = i + 1

with open("/home/alex_anast/workspace/advent_of_code_2022/day3/input_data") as my_file:
    contents = my_file.readlines()

sum = 0

for rucksack in contents:
    rucksack = rucksack[:-1]
    assert len(rucksack) % 2 == 0

    # That's the reformatting of Black, p.s. I don't like it that much
    sum = (
        sum
        + hash_table[
            findWrong(
                rucksack[: int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2) :]
            )
        ]
    )

print(sum)
