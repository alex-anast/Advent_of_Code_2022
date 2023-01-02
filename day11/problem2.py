from math import floor
from re import findall
# from decimal import Decimal
import math

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
    
    def throwItem(self, monkey_id: int, item: int, lm = list_monkeys):
        monkey = lm[monkey_id]
        monkey.starting_items.append(item)
    
    def popItem(self):
        self.starting_items.reverse()
        item = self.starting_items.pop()
        self.starting_items.reverse()
        return item
    
def round(verbose=False, divide_by_three=False):
    for monkey in list_monkeys:
        # It's easier to pop the item before throwing stuff around.
        while monkey.starting_items:
            item = monkey.popItem() 
            monkey.inspected_items += 1

            if verbose:
                print("Monkey {}:".format(monkey.id))
                print("\tMonkey inspets an item with a worry level {}.".format(item))

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
                
            if divide_by_three: # This no longer happens
                current_worry_level = floor(result / 3)
            else:
                current_worry_level = result
                        
            # current_worry_level = result
            if verbose:
                print("\tMonkey no longer gets bored with item. Worry level is NOT divided by 3, it remains {}.".format(current_worry_level))
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

def printMonkeys(show_items=False):
    if show_items:
        print("----- ----- ----- ----- ----- -----")
        for monkey in list_monkeys:
            print("Monkey {}: Inspected {}, \titems {}".format(monkey.id, monkey.inspected_items, monkey.starting_items))
        print("----- ----- ----- ----- ----- -----")
    else:
        for monkey in list_monkeys:
            print("Monkey {} inspected items {} times.".format(monkey.id, monkey.inspected_items))
        
def toneDown(lcm):
    ## # Approach No1:
    ## # One idea was to work with the Decimal library but it imposes the same problem: too long numbers.
    ## for monkey in list_monkeys:
    ##     for i, _ in enumerate(monkey.starting_items):
    ##         if len(str(tem)) > 9:
    ##             item = Decimal(str(item))
    ##             divide_with = Decimal('10')
    ##             quotient = item / divide_with
    ##             print(quotient)

    ## # Approach No2:
    ## # Another idea was to impose a limit. But this limits only the huge numbers, which changes slightly the algorithm.
    ## # monkey.starting_items[i] = item % 100000000000

    ## # Approach No3:
    ## # What if we remove the least significant bit(s)? ... Nope.
    ## try:
        ## monkey.starting_items[i] = int(str(item)[:-20])
        ## # print(monkey.starting_items[i])
    ## except:
        ## raise Exception
                
    # The best method I can think of is to divide in EACH round with the Least Common Multiple.
    # This way, I am never going to break the algorithm but hopefully I can keep the numbers down
    #      to a reasonable amount.
    # ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
    # You can use the modulo operator and the LCM together in Python to perform various arithmetic operations
    # involving large integers. For example, you might use the modulo operator to find the remainder of a
    # division operation involving large integers, and then use the LCM to determine the least common multiple
    # of the result and another integer. This can be useful when you need to work with large integers in Python
    # and need to ensure that the results of your arithmetic operations are accurate and consistent.
    # ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
    for monkey in list_monkeys:
        for i in range(len(monkey.starting_items)):
            try:
                monkey.starting_items[i] %= lcm
            except ValueError as ve:
                print("The number has become obsolete: {}".format(ve))
                raise

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

"""
Run the Rounds and print the aftermath: (sort of like a main)
"""
lcm = 1
for monkey in list_monkeys:
    lcm = lcm * monkey.test // math.gcd(lcm, monkey.test)

for rd in range(1, 10001):
    if rd == 1:
        round(verbose=True)
    else:
        round()
    toneDown(lcm)
    if rd in (1, 20, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000):
        print("\n== After round {} ==".format(rd))
        printMonkeys()
        # printMonkeys(show_items=True)

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
