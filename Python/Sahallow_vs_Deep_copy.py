import copy

initial_list  = [1, 2, [3, 2]]

#copyed_list = copy.copy(initial_list)
copyed_list = copy.deepcopy(initial_list)

initial_list[0] = 5
initial_list[2][0] = 6

print(initial_list)
print(copyed_list)