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
                 if_false:          int     = -1,
                 inspected_items:   int     = 0
                 ):
        self.id = id
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_items = inspected_items
    
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
        self.starting_items.reverse()
        for i in range(how_many):
            self.starting_items.pop()
        self.starting_items.reverse()
     
    def round(self, verbose=False):
        for monkey in list_monkeys:
            # It's easier to pop the item before throwing stuff around.
            while monkey.starting_items:
                item = monkey.popItem() 
                monkey.inspected_items += 1

                if verbose:
                    print("Monkey {}:".format(monkey.id))
                    print("\tMonkey inspects an item with a worry level {}.".format(item))

                # keep the "old" for reusability
                if monkey.operation[0] == "old":
                    temp_op = int(item)
                else:
                    temp_op = int(monkey.operation[0])
                # There has to be a smarter way
                if monkey.operation[1] == "increases":
                    result = int(item) + temp_op
                elif monkey.operation[1] == "decreases":
                    result = int(item) - temp_op
                elif monkey.operation[1] == "is multiplied":
                    result = int(item) * temp_op
                elif monkey.operation[1] == "is divided":
                    result = int(item) / temp_op
                if verbose:
                    print("\tWorry level {} by {} to {}.".format(
                        monkey.operation[1],
                        temp_op,
                        result
                    ))
        
                current_worry_level = floor(result / 3)
                if verbose:
                    print("\tMonkey gets bored with item. Worry level is divided by 3 to {}.".format(current_worry_level))
                arg1 = ""
                arg2 = True
                if current_worry_level % monkey.test == 0:
                    arg1 = "is divisible"
                else:
                    arg1 = "is NOT divisible"
                    arg2 = False
                if verbose:
                    print("\tCurrent worry level {} by {}.".format(arg1, monkey.test))
                if arg2:    # choose if_true
                    if verbose:
                        print("\tItem with worry level {} is thrown to monkey {}.\n".format(current_worry_level, monkey.if_true))
                    monkey.throwItem(monkey.if_true, current_worry_level)
                else: 
                    if verbose:
                        print("\tItem with worry level {} is thrown to monkey {}.\n".format(current_worry_level, monkey.if_false))
                    monkey.throwItem(monkey.if_false, current_worry_level)
    
    def throwItem(self, monkey_id: int, item: int, lm = list_monkeys):
        monkey = lm[monkey_id]
        monkey.starting_items.append(item)
    
    def popItem(self):
        self.starting_items.reverse()
        item = self.starting_items.pop()
        self.starting_items.reverse()
        return item

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

def printMonkeys():
    print("----- ----- ----- ----- ----- -----")
    for i, monkey in enumerate(list_monkeys):
        # monkey.clearItems(monkey.countItems())
        print("Monkey {}: Inspected {}, \titems {}".format(monkey.id, monkey.inspected_items, monkey.starting_items))
    print("----- ----- ----- ----- ----- -----")

with open(
    # "/mnt/shared/code/day11/input_0.conf"
    "/mnt/shared/code/day11/input.conf"
    ) as my_file:
    contents = my_file.readlines()

"""
Create all monkeys and put them in a list
The monkey's number is the id of the list
"""
for i, monkey_id in enumerate(range(0, len(contents), 7)):
    # create object
    monkey = Monkey(
        id=i,
        starting_items=tokenize(contents[monkey_id+1])[2:],
        operation=createOperationFunction(contents[monkey_id+2]),
        test=int(tokenize(contents[monkey_id+3])[-1]),
        if_true=int(tokenize(contents[monkey_id+4])[-1]),
        if_false=int(tokenize(contents[monkey_id+5])[-1])
    )
    list_monkeys.append(monkey)
    # break

"""
Run the Rounds and print the aftermath: (sort of like a main)
"""
for rd in range(1, 21):
    if rd == 1:
        monkey.round(verbose=True)
    else:
        monkey.round()
    if rd == 1 or rd == 10 or rd == 15 or rd == 20:
        print("ROUND ", rd)
        printMonkeys()

"""
Calculate Monkey Business
"""
temp_ls = []
for monkey in list_monkeys:
    temp_ls.append(monkey.inspected_items)

temp_ls.sort()
item1 = temp_ls.pop()
item2 = temp_ls.pop()
monkey_buiness = item1 * item2
print(monkey_buiness)
