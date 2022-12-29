with open(
    "/home/user/workspace/99_my_workspace/day7/input_data_0.bash"
    ) as my_file:
    contents = my_file.readlines()

tree = {}
tree["0"] = {"/"}

def cd(cmd, tree) -> str:
    cmd = cmd.split()
    if cmd[1] == "..":
        # Not sure, but it should return the previous level
        # ...since the key of the dict is the depth index
        return [x-1 for x in tree.keys() if tree[x] == '..'][0]
    elif cmd[1] == "/":
        # root is index 0 always
        return '0'
    else:
        # ... maybe it's better to have the level as value
        # ... because you can't actively search for it!
        pass

for line in contents:
    if "cd" in line:
        pass