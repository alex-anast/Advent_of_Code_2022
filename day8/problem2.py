# I want to create a two dimensional matrix


def createMatrix(contents) -> list:
    matrix_trees = []
    for row in contents:
        row = list(row[:-1])
        # Then give it as a single element to the matrix_tree
        matrix_trees.append(row)
    return matrix_trees


def printMatrix(matrix) -> None:
    for row in matrix:
        print(row)


def printTranspose(matrix) -> None:
    transposed = [list(col) for col in zip(*matrix_objects)]
    for row in transposed:
        print(row)


with open("/home/alex_anast/workspace/advent_of_code_2022/day8/input") as my_file:
    contents = my_file.readlines()

matrix_tree = createMatrix(contents)
# printMatrix(matrix_tree)


class Tree:
    def __init__(
        self,
        row,
        column,
        v_l: bool = False,
        v_r: bool = False,
        v_t: bool = False,
        v_b: bool = False,
        height: int = 0,
        d_l: int = 0,
        d_r: int = 0,
        d_t: int = 0,
        d_b: int = 0,
    ):
        self.row = row
        self.column = column
        self.v_l = v_l
        self.v_r = v_r
        self.v_t = v_t
        self.v_b = v_b
        self.d_l = d_l
        self.d_r = d_r
        self.d_t = d_t
        self.d_b = d_b
        self.height = height

    def visibleFromLeft(self, matrix_objects) -> None:
        self.v_l = True
        if self.column > 0:
            temp_id = self.column - 1
            while temp_id >= 0:
                if matrix_objects[self.row][temp_id].height >= self.height:
                    # print(f"{matrix_objects[self.row][temp_id].height} > {self.height}")
                    self.v_l = False
                    break  # optimization
                temp_id = temp_id - 1

    def visibleFromRight(self, matrix_objects) -> None:
        self.v_r = True
        if self.column < len(matrix_objects[0]) - 1:
            temp_id = self.column + 1
            while temp_id <= len(matrix_objects[0]) - 1:
                if matrix_objects[self.row][temp_id].height >= self.height:
                    self.v_r = False
                    break  # optimization
                temp_id = temp_id + 1

    def visibleFromTop(self, matrix_objects) -> None:
        # Let's take advantage from the fact that the input data is a square matrix:
        transposed = [list(col) for col in zip(*matrix_objects)]
        self.v_t = True
        if self.row > 0:
            temp_id = self.row - 1
            while temp_id >= 0:
                # print(f"{transposed[self.column][temp_id].height} > {self.height}")
                if transposed[self.column][temp_id].height >= self.height:
                    self.v_t = False
                    break  # optimization
                temp_id = temp_id - 1

    def visibleFromBottom(self, matrix_objects) -> None:
        transposed = [list(col) for col in zip(*matrix_objects)]
        self.v_b = True
        if self.row < len(transposed[0]) - 1:
            temp_id = self.row + 1
            while temp_id <= len(transposed[0]) - 1:
                if transposed[self.column][temp_id].height >= self.height:
                    self.v_b = False
                    break  # optimization
                temp_id = temp_id + 1

    def printVerbose(self) -> None:
        print(f"\n=== Height:\t{self.height}")
        print(f"Row:  {self.row}, Column:  {self.column}")
        # print(f"Visible from Left:\t{self.v_l}")
        # print(f"Visible from Right:\t{self.v_r}")
        # print(f"Visible from Top:\t{self.v_t}")
        # print(f"Visible from Bottom:\t{self.v_b}")
        print(f"Distance from Left:\t{self.d_l}")
        print(f"Distance from Right:\t{self.d_r}")
        print(f"Distance from Top:\t{self.d_t}")
        print(f"Distance from Bottom:\t{self.d_b}")

    def checkVisibility(self) -> bool:
        if self.v_l or self.v_r or self.v_t or self.v_b:
            return True
        else:
            return False

    def distanceFromLeft(self, matrix_objects):
        self.d_l = 0
        for i in reversed(range(self.column)):
            self.d_l = self.d_l + 1
            if matrix_objects[self.row][i].height >= self.height:
                break

        ## # Now I have to keep the index of the one that I meet in the direction I see
        ## # This can be really complex if I continue solving it like I am writing C
        ## # So, let's try to use some Pythonism instead:
        ## ### UPDATE
        ## # This way, it keeps a reference so you can check for all the trees
        ## # but the problem is way fucking simpler by data input:
        ## # "stop if you reach an edge or at the first tree that is the same height"
        ## # "or taller than the tree under consideration."
        ## reference = self.height
        ## self.d_l = 0
        ## has_changed = False
        ## for i in reversed(range(self.column)):
        ##     self.d_l = self.d_l + 1
        ##     if matrix_objects[self.row][i].height > reference:
        ##         reference = matrix_objects[self.row][i].height
        ##         has_changed = True
        ##     else:
        ##         if has_changed:
        ##             self.d_l = self.d_l - 1
        ##             break

    def distanceFromRight(self, matrix_objects):
        self.d_r = 0
        for i in range(self.column + 1, len(matrix_objects[self.row])):
            self.d_r = self.d_r + 1
            if matrix_objects[self.row][i].height >= self.height:
                break

    def distanceFromTop(self, matrix_objects):
        transposed = [list(col) for col in zip(*matrix_objects)]
        self.d_t = 0
        for i in reversed(range(self.row)):
            self.d_t = self.d_t + 1
            if transposed[self.column][i].height >= self.height:
                break

    def distanceFromBottom(self, matrix_objects):
        transposed = [list(col) for col in zip(*matrix_objects)]
        self.d_b = 0
        for i in range(self.row + 1, len(transposed[self.column])):
            self.d_b = self.d_b + 1
            if transposed[self.column][i].height >= self.height:
                break


matrix_objects = []
for row_id, matrix_row in enumerate(matrix_tree):
    matrix_tree_row_w_classes = []
    for i, v in enumerate(matrix_row):
        obj = Tree(row=row_id, column=i)
        obj.height = v
        matrix_tree_row_w_classes.append(obj)

    matrix_objects.append(matrix_tree_row_w_classes)
    # print(row_id, matrix_row)

# # Set Visibility boolean parameter of object -> Tree
# count = 0
# for row_id in range(len(matrix_objects)):
#     for column_id in range(len(matrix_objects[row_id])):
#         matrix_objects[row_id][column_id].visibleFromLeft(matrix_objects)
#         matrix_objects[row_id][column_id].visibleFromRight(matrix_objects)
#         matrix_objects[row_id][column_id].visibleFromTop(matrix_objects)
#         matrix_objects[row_id][column_id].visibleFromBottom(matrix_objects)
#         if matrix_objects[row_id][column_id].checkVisibility():
#             count = count + 1
# print(count)

dict_calc = {}
for row_id in range(len(matrix_objects)):
    for column_id in range(len(matrix_objects[row_id])):
        matrix_objects[row_id][column_id].distanceFromLeft(matrix_objects)
        matrix_objects[row_id][column_id].distanceFromRight(matrix_objects)
        matrix_objects[row_id][column_id].distanceFromTop(matrix_objects)
        matrix_objects[row_id][column_id].distanceFromBottom(matrix_objects)
        dict_calc[f"{row_id},{column_id}"] = (
            matrix_objects[row_id][column_id].d_l
            * matrix_objects[row_id][column_id].d_r
            * matrix_objects[row_id][column_id].d_t
            * matrix_objects[row_id][column_id].d_b
        )

# from pprint import pprint
# pprint(dict_calc)

print(max(dict_calc.values()))

# DISCLAIMER
# It would be interesting to use tupple unpacking in the case of such problems too.
# Dictionaries:
# for key, value in my_dict.items():
#   ...work with either (been looking for it)
#
# If I was smarter, the input data would be organized as a list of Tupples, and not list of lists:
# [
#  (X, X, X),
#  (X, X, X),
#  (X, X, X)
# ]
