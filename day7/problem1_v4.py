if input() == ' ':
    FILE = "/home/alex_anast/workspace/advent_of_code_2022/day7/input"
else:
    FILE = "/home/alex_anast/workspace/advent_of_code_2022/day7/input_0"

with open(FILE) as my_file:
    contents = my_file.readlines()

def createLine(line) -> list:
    # assuming line has a \n in the end
    # Test specifically for blank!
    return (line[:-1]).split(" ")

def testDuplicateDirectories(list_directories) -> bool:
    try:
        assert(len(set(list_directories)) == len(list_directories))
        return True
    except AssertionError:
        print("List elements not unique, printing duplicates:\n")
        import collections
        print([item for item, count in collections.Counter(list_directories).items() if count > 1])
        return False

def listDirectories(contents):
    list_directories = []
    for line in contents:
        line = createLine(line)
        if line[0] == '$':
            # print("Command:\t{}".format(line[1]))
            if line[1] == "cd":
                # print("Directory:\t{}".format(line[2]))
                if line[2] != "..":
                    list_directories.append(line[2])
    return list_directories

list_directories = listDirectories(contents)
# print(list_directories)

#TEST
if testDuplicateDirectories(list_directories):
    print("No duplicates found.")
# ===== ===== ===== ===== =====
# Personal notes about debugging..
# So, the original input file has duplicates.
# ===== ===== ===== ===== =====



if FILE[-1:] == '0':
    print("\n\ndemo")
else:
    print("\n\nofficial")

    