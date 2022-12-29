class Directory:
    def __init__(self, name, depth, size=None, parent="", children=[], id=0):
        self.name = name
        self.depth = depth
        self.size = size
        self.parent = parent
        self.children = children
        self.id = id
    
    def findChildren(self, contents_split):
        self.children = []
        for i in range(self.id+1, len(contents_split)):
            if contents_split[i][0] == '$':
                break
            elif contents_split[i][0] == "dir":
                self.children.append(contents_split[i][1])
            else:
                # What happens at the end of the file?
                raise Exception

    def findParent(self, location, contents_split):
        pass

    def printInfo(self):
        print("self.name\t{}".format(self.name))
        print("self.depth\t{}".format(self.depth))
        print("self.size\t{}".format(self.size))
        print("self.parent\t{}".format(self.parent))
        print("self.children\t{}".format(self.children))
        print("self.id\t\t{}".format(self.id))
        
def getCleanContents(contents) -> list:
    clean_contents = []
    for line in contents:
        line = line[:-1].split(" ")
        clean_contents.append(line)
    return clean_contents

def printList(ls):
    for element in ls:
        print(element)


# OPEN FILE
if input() == ' ':
    # Enter space for official
    FILE = "/home/alex_anast/workspace/advent_of_code_2022/day7/input"
else: # Just click enter for demo
    FILE = "/home/alex_anast/workspace/advent_of_code_2022/day7/input_0"
with open(FILE) as my_file:
    contents = my_file.readlines()


clean_contents = getCleanContents(contents)
# printList(clean_contents)

root = Directory(name='/', depth=0, parent=None, id=0)
root.findChildren(clean_contents)

root.printInfo()


if FILE[-1:] == '0':
    print("\n\ndemo")
else:
    print("\n\nofficial")