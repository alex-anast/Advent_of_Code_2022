"""
===== PART TWO =====

Groups of 3
Every group carries the same item_type (all 3)
common between all three Elves


"""


def findWrong(c1, c2) -> str:
    for item_type_1 in c1:
        for item_type_2 in c2:
            if item_type_1 == item_type_2:
                return item_type_1


def findCommon(group) -> str:
    return set(group[0][:-1]) & set(group[1][:-1]) & set(group[2][:-1])


hash_table = {}

for i in range(52):
    # 'A' => 65 'Z' => 90 ...  'a' => 97 'z' => 122
    if i <= 25:
        hash_table[chr(65 + i).lower()] = i + 1
    else:
        hash_table[chr(71 + i).upper()] = i + 1

with open("/home/alex_anast/workspace/advent_of_code_2022/day3/input_data") as my_file:
    contents = my_file.readlines()

groups = [
    (contents[i], contents[i + 1], contents[i + 2]) for i in range(0, len(contents), 3)
]

sum = 0

for group in groups:
    result = findCommon(group)
    # print(type(str(result)), str(result))

    sum = sum + hash_table[str(result)[2]]

print(sum)
