from pathlib import Path
import os

with open(
    "/home/user/workspace/99_my_workspace/day7/input_data_0.bash"
    ) as my_file:
    contents = my_file.readlines()

root = Path("root")

set_of_commands = set()

for line in contents:
    if line[0] == '$':
        set_of_commands.add(line[2:-1])

print(set_of_commands)

root_dir = "root"
os.makedirs(root_dir)
tree = {}

for command in set_of_commands:
    command = command.split()
    print(command)
    if len(command) == 2:
        # cd <where>
        if command[1] == "..":
            pass
        elif command[1] == "/":
            pass
        else:
            # if dir exists in dictionary:
            # else: mkdir    
            pass
            
    else:
        # ls
        pass
    

# It would be really nice to implement this with classes too.
# Maybe a full directory is a dictionary
# (and further directories are further dictionaries)