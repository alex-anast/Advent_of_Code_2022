# ===== ===== ADVENT OF CODE ===== ===== 
# 
# Let's play around with dictionaries for this problem.
# 
# ===== ===== ============== ===== ===== 

with open(
    "/home/alex_anast/workspace/advent_of_code_2022/day7/input_data.bash"
    ) as my_file:
    contents = my_file.readlines()

starting_point = True
directory = []
dir_sum = 0
dir_dictionary = {}
dir_dictionary_parent = {}
command_previous = False
working_dir = ""
for bash_line in contents:
    bash_detailed = (bash_line[:-1]).split(" ")
    if bash_detailed[0] ==  '$':
        if not command_previous and not starting_point:
            dir_dictionary_parent[working_dir].update(dir_dictionary)
            dir_dictionary = {}
        starting_point = False
        command_previous = True
        if bash_detailed[1] == "cd":
            if bash_detailed[2] == "..":
                # TODO
                pass
            else:
                dir_dictionary_parent.update({bash_detailed[2] : {}})
                working_dir = bash_detailed[2]
        elif bash_detailed[1] == "ls":
            # TODO
            pass
        else:
            raise Exception
    else:
        command_previous = False
        if bash_detailed[0] == "dir":
            dir_dictionary.update({bash_detailed[1]:bash_detailed[0]})
        else:
            dir_dictionary.update({bash_detailed[1]:int(bash_detailed[0])})
dir_dictionary_parent[working_dir].update(dir_dictionary)

# print(directory)
# from json import dumps
# print(dumps(dir_dictionary_parent, indent=2))
print(len(dir_dictionary_parent))

# So now, the whole root directory has been mapped.
dir_points = {}
for dict_in_dict in dir_dictionary_parent.values():
    while "dir" in dict_in_dict.values():
        # print("===== ===== ===== ===== =====")
        for keys, values in dir_dictionary_parent.items():
            if "dir" not in values.values():
                # print("Working key is : ", keys)
                sum_size = 0
                for size in values.values():
                    sum_size += size
                dir_points.update({keys : sum_size})
            else:
                for key_i, v_i in dir_points.items():
                    if key_i in values.keys():
                        dir_dictionary_parent[keys][key_i] = v_i
# let's manually add the root
sum_size = 0
for values in dir_dictionary_parent['/'].values():
    sum_size += values
dir_points.update({'/' : sum_size})

# Printing stuff
for keys, values in dir_dictionary_parent.items():
    print(keys, values) 
print(dir_points) 

dir_size_total = {}
for keys, values in dir_dictionary_parent.items():
    total_sum_size = 0
    for each in values.values():
        total_sum_size += each
    dir_size_total[keys] = total_sum_size
    
for keys, values in dir_dictionary_parent.items():
    print(keys, values) 
print()

sum_final = 0
for keys, values in dir_size_total.items():
    print(keys, values) 
    if values <= 100000:
        print("===>", keys, values)
        sum_final += values
print()
print(sum_final)
