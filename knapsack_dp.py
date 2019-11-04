""" Knapsack problem https://en.wikipedia.org/wiki/Knapsack_problem
(Best choice of items for knapsack in 0-1 Knapsack Problem) """

# This is dynamic programming solution, time complexity is O(nW), where "n" is 
# number of items, "W" is maximum weight of knapsack.

import time

# Maximum weight of knapsack
knapsack = 20

# Items = [(value1, weight1), (value2, weight2), ...]
items = [
    (1, 1),
    (11, 10),
    (4, 7),
    (9, 10),
    (2, 3),
    (2, 7),
    (10, 9),
    (7, 6),
    (4, 5),
    (15, 17),
    (10, 10)
]
def best_choice_for_knapsack(items, max_weight):
    # Forming the table which will be filled later. Each index of table is weight
    # of item minus 1 since index starts from 0. 
    table = [(0, [(0, 0)]) for e in range(0, max_weight)]
    # Calculating and storing the best sum of values for each weight (index of 
    # the table). 
    for e in items: 
        # Index (i) of the table is a weight of item or sum of weights of 
        # items, minus 1 since index starts from 0. 
        for i in range(0, max_weight):
            # There is no item of this weight (i of table) if table[i][0] == 0 
            if table[i][0] != 0:
                sum_of_values = e[0] + table[i][0]
                sum_of_weights = e[1] + i
                # Example of table: [
                # (value1, [(value1, weight1)]), ... 
                # (sum_of_values, [(value1, weight1), (value2, weight2)])
                # ]
                if sum_of_weights + 1 <= max_weight and \
                table[sum_of_weights][0] < sum_of_values:
                    table[sum_of_weights] = \
                        (sum_of_values, [e] + table[i][1])
        # Storing item in table if its value is bigger than stored sum of items 
        if table[e[1] - 1][0] < e[0]:
            table[e[1] - 1] = (e[0], [e])
    mx = max(table)
    print('Best value is ' + str(mx[0]))
    return 'Best combination is ' + str(mx[1]) + '\n'

# Measuring the time of execution
start = time.time()
print(best_choice_for_knapsack(items, knapsack))
end = time.time()
print('Time of execution is ' + str(end - start))


