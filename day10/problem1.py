"""
addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
noop takes one cycle to complete. It has no other effect.
"""

with open(
        # "/home/user/workspace/99_my_workspace/day10/input_0"
        # "/home/user/workspace/99_my_workspace/day10/input_1"
        "/home/user/workspace/99_my_workspace/day10/input_2"
    ) as my_file:
    contents = my_file.readlines()

# NOT GONNA WORK EASILY
# count_cycles = 0
# X_register = 1
# for command in contents:
#     command = command[:-1].split(" ")
#     if len(command) == 1:
#         count_cycles += 1
#     else:
#         count_cycles += 2
#         # Writing it analytically because the value added can also be negative
#         X_register = X_register + (int(command[1]))

# TODO
# Because of the nature of the cycles,
# it is more correct to write a while True poll loop function and then wait unti all the input has finished.
# This way you can catch a cycle (i.e. 20th) that the command addx hasn't finished yet.
# With for loop I would need a bunch of checks to implement it.
# Let's try:

# import logging
# logging.basicConfig(filename='problem1.log', filemode='w', level=logging.INFO)

# not exactly a poll loop
# I notice that intuitively I solve it like I am writing C code..
iteration = 0
cycle = 0
X_register = 1
flag = False
sum_signal_strength = 0
while True:
    try:
        cycle += 1 # whatever happens, cycle is running
        # print(((contents[iteration])[:-1]).split(" "))
        command = ((contents[iteration])[:-1]).split(" ")

        # Another nice example where I could use match - case but I work on Debian 9 and Python 3.5.3
        if cycle in (20,60,100,140,180,220):
            # print(cycle*X_register)
            sum_signal_strength += cycle*X_register
        
        if len(command) == 1:
            # do nothing. Just eat up a cycle
            iteration += 1
        else: # addx is in command
            if not flag: # First time will be False
                flag = True
                # Don't increment iteration because you want one more cycle in the same command
            else: # Do stuff and set to false again if completed
                flag = False
                iteration += 1

                # IMPLEMENTATION
                X_register += int(command[1])
    
    except IndexError as ie:
        # logging.info("{}: End Of File.".format(ie))
        print("{}: End Of File.".format(ie))
        break
    except Exception as wtf:
        print(wtf)

print("\nFinal amount:\t", X_register)
print("Sum of the Signal Strenghts is\t", sum_signal_strength)

