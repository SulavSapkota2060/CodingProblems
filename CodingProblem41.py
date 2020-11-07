#INCOMPLETE

initial_list =    [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
new_list = []
def get_itenary(flight,starting_point):
    global new_list
    new_list = [starting_point]
    for f in flight:
        for i in range(0,len(initial_list)):
            if new_list[-1] in initial_list[i][0]:
                new_list.append(initial_list[i][0])




print(new_list)