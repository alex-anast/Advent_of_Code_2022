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
    ):
        self.row = row
        self.column = column
        self.v_l = v_l
        self.v_r = v_r
        self.v_t = v_t
        self.v_b = v_b
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
        print(f"Left:\t{self.v_l}")
        print(f"Right:\t{self.v_r}")
        print(f"Top:\t{self.v_t}")
        print(f"Bottom:\t{self.v_b}")

    def checkVisibility(self) -> bool:
        if self.v_l or self.v_r or self.v_t or self.v_b:
            return True
        else:
            return False


matrix_objects = []
for row_id, matrix_row in enumerate(matrix_tree):
    matrix_tree_row_w_classes = []
    for i, v in enumerate(matrix_row):
        obj = Tree(row=row_id, column=i)
        obj.height = v
        # And here add if it is visible from all directions
        # ... can't I should first have created the matrix with the way it is being implemented
        matrix_tree_row_w_classes.append(obj)

    matrix_objects.append(matrix_tree_row_w_classes)
    # print(row_id, matrix_row)

# Set Visibility boolean parameter of object -> Tree
count = 0
for row_id in range(len(matrix_objects)):
    for column_id in range(len(matrix_objects[row_id])):
        matrix_objects[row_id][column_id].visibleFromLeft(matrix_objects)
        matrix_objects[row_id][column_id].visibleFromRight(matrix_objects)
        matrix_objects[row_id][column_id].visibleFromTop(matrix_objects)
        matrix_objects[row_id][column_id].visibleFromBottom(matrix_objects)
        if matrix_objects[row_id][column_id].checkVisibility():
            count = count + 1

print(count)
