def findMatrixSize(contents) -> list:
    R = L = U = D = 0
    for i in contents:
        temp = i.split()
        if temp[0] == 'R':
            R += int(temp[1])
        elif temp[0] == 'L':
            L += int(temp[1])
        elif temp[0] == 'U':
            U += int(temp[1])
        elif temp[0] == 'D':
            D += int(temp[1])
        else:
            raise Exception("Doesn't belong aywhere!")
    print("\n\
          Right\t{}\n\
          Left\t{}\n\
          Up\t{}\n\
          Down\t{}\n\
          Max ==>\t{}\n\
          ".format(R,L,U,D,max([R,L,U,D])))
    return [R,L,U,D]

def fillMatrixWithDots(contents) -> list:
    playing_table = []
    matrix_size = findMatrixSize(contents)
    for i in range(matrix_size[2] + matrix_size[3]):
        for j in range(matrix_size[0] + matrix_size[1]):
            print(i,j)
            playing_table[i][j].append(".")
    return playing_table
    
with open(
    "/home/user/workspace/99_my_workspace/day9/data_0"
    ) as my_file:
    contents = my_file.readlines()

# Maybe this is a great opportunity to play with NumPy (see chatGPT)
playing_table = fillMatrixWithDots(contents)
for i in playing_table:
    print(i)