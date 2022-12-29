from math import floor
from re import findall

list_monkeys = []

class Monkey:
    def __init__(self,
                 id:                int     = -1,
                 starting_items:    list    = [],
                 operation:         str     = [],
                 test:              int     = 1,
                 if_true:           int     = -1,
                 if_false:          int     = -1
                 ):
        self.id = id
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
    
    def printMonkey(self):
        print("MonkeyNo  \t{}".format(self.id))
        print("StartItems\t{}".format(self.starting_items))
        print("Operation \t{}".format(self.operation))
        print("Test      \t{}".format(self.test))
        print("If True   \t{}".format(self.if_true))
        print("If False  \t{}".format(self.if_false))
    
    def countItems(self):
        return len(self.starting_items)
    
    def clearItems(self, how_many = 0):
        self.starting_items = self.starting_items.reverse()
        print(self.starting_items)
        for i in range(how_many):
            self.starting_items.pop(i)
        self.starting_items.reverse()
        print(self.starting_items)
     
    def round(self):
        for i, item in enumerate(monkey.starting_items):
            print("Monkey {}:".format(monkey.id))
            print("\tMonkey inspects an item with a worry level {}.".format(item))

            # I want to keep the "old" for reusability
            if monkey.operation[0] == "old":
                temp_op = int(item)
            else:
                temp_op = int(monkey.operation[0])
            # Have to check what happens for "old" in operation
            # Come on... there has to be a smarter way
            result = 0
            if monkey.operation[1] == "increases":
                result = int(item) + temp_op
            elif monkey.operation[1] == "decreases":
                result = int(item) - temp_op
            elif monkey.operation[1] == "is multiplied":
                result = int(item) * temp_op
            elif monkey.operation[1] == "is divided":   # could also use else
                result = int(item) / temp_op
            print("\tWorry level {} by {} to {}.".format(
                monkey.operation[1],
                temp_op,
                result
            ))
        
            current_worry_level = floor(result / 3)
            print("\tMonkey gets bored with item. Worry level is divided by 3 to {}.".format(current_worry_level))
            arg1 = ""
            arg2 = True
            if current_worry_level % monkey.test == 0:
                arg1 = "is divisible"
            else:
                arg1 = "is NOT divisible"
                arg2 = False
            print("\tCurrent worry level {} by {}.".format(arg1, monkey.test))
            if arg2:    # choose if_true
                print("\tItem with worry level {} is thrown to monkey {}.".format(current_worry_level, monkey.if_true))
                monkey.throwItem(monkey.if_true, current_worry_level)
            else: 
                print("\tItem with worry level {} is thrown to monkey {}.".format(current_worry_level, monkey.if_false))
                monkey.throwItem(monkey.if_false, current_worry_level)
            print() 
    
    def throwItem(self, monkey_id: int, item: int, lm = list_monkeys):
        monkey = lm[monkey_id]
        monkey.starting_items.append(item)
        

def tokenize(string):
    return findall(r'\b\w+\b', string)

def createOperationFunction(operation: str) -> list:
    math_op = ''
    if '+' in operation:
        math_op = "increases"
    elif '-' in operation:
        math_op = "decreases"
    elif '*' in operation:
        math_op = "is multiplied"
    elif '/' in operation:
        math_op = "is divided"
    else:
        raise ValueError
    operation = tokenize(operation)
    return [operation[-1], math_op]

with open("/mnt/shared/code/day11/input_0") as my_file:
    contents = my_file.readlines()

# -----
# Create all monkeys and put them in a list
# The monkey's number is the id of the list
# -----
for monkey_id in range(0, len(contents), 7):
    # create object
    monkey = Monkey(
        id= monkey_id % 6, # six lines
        starting_items=tokenize(contents[monkey_id+1])[2:],
        operation=createOperationFunction(contents[monkey_id+2]),
        test=int(tokenize(contents[monkey_id+3])[-1]),
        if_true=int(tokenize(contents[monkey_id+4])[-1]),
        if_false=int(tokenize(contents[monkey_id+5])[-1])
    )
    list_monkeys.append(monkey)
    # break

# ROUND 1
how_many_before = []
for monkey in list_monkeys:
    how_many_before.append(monkey.countItems())
print(how_many_before)
for monkey in list_monkeys:
    monkey.round()
print("----- ----- -----")
for i, monkey in enumerate(list_monkeys):
    monkey.clearItems(how_many_before[i])
    print("Monkey {}: {}".format(monkey.id, monkey.starting_items))
print("----- ----- -----")