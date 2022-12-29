s1 = ['Z', 'P', 'M', 'H', 'R']
s2 = ['P', 'C', 'J', 'B']
s3 = ['S', 'N', 'H', 'G', 'L', 'C', 'D']
s4 = ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L']
s5 = ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M']
s6 = ['T', 'F', 'S', 'Z', 'B', 'G']
s7 = ['N', 'R', 'V']
s8 = ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M']
s9 = ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
stack_of_stacks = [s1,s2,s3,s4,s5,s6,s7,s8,s9]

# s1 = ['Z', 'N']
# s2 = ['M', 'C', 'D']
# s3 = ['P']
# stack_of_stacks = [s1,s2,s3]

with open("/home/user/workspace/99_my_workspace/day5/movements") as (my_file):
    contents = my_file.readlines()

for movement in contents:
    movement = movement.split()[1::2]
    
    temp_list = []
    for times in range(int(movement[0])):
        assert(len(stack_of_stacks[int(movement[1])-1])>0)
        
        temp_list.append(
            stack_of_stacks[
            int(movement[1])-1
            ].pop()
        )

    for crane in temp_list[::-1]:
        stack_of_stacks[int(movement[2])-1 ].append(crane)
    
print("===== FINAL =====")
for stack in stack_of_stacks:
    print(stack)
print()

final = []
for s in stack_of_stacks:
    final.append(s[-1])
final = "".join(final)
print(final)