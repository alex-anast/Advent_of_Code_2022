def ifEncloses(ad1, ad2) -> bool:
    if int(ad1[0]) <= int(ad2[0]) and int(ad1[1]) >= int(ad2[1]):
        return True

def ifOverlaps(ad1, ad2) -> bool:
    if int(ad1[0]) >= int(ad2[0]) and int(ad1[0]) <= int(ad2[1]):
        return True
    elif int(ad1[1]) >= int(ad2[0]) and int(ad1[0]) <= int(ad2[1]):
        return True
    else:
        return False

with open(
    "/home/user/workspace/99_my_workspace/day4/input_data"
) as my_file:
    contents = my_file.readlines()

count = 0

for pair in contents:
    pair = pair.split(',')
    pair[1] = pair[1][:-1]

    assignment_1 = pair[0]
    assignment_2 = pair[1]
    ass_detailed_1 = assignment_1.split('-')
    ass_detailed_2 = assignment_2.split('-')

    if ifOverlaps(ass_detailed_1, ass_detailed_2):
        count = count+1
        # print(count, "\t\t", ass_detailed_1, " -- ", ass_detailed_2)
        # print(count, "\t\t", ass_detailed_2, " -- ", ass_detailed_1)
        # print()
        
print(count)
