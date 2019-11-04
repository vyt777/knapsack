""" Knapsack problem https://en.wikipedia.org/wiki/Knapsack_problem
(Best choice of items for knapsack in 0-1 Knapsack Problem) """

# This is brute-force decision, time complexity is O(n!).
# Keeping this solution for experimental purposes. :-)

from itertools import permutations
import time

# maximum weight of knapsack
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
# Attention: time of execution with this items selection is 46 seconds on my 
# machine !

def best_choice_for_knapsack(items, max_weight):
    combinations = permutations(items, len(items))
    best_choice = []
    best_ratio = 0
    for combination in combinations:
        remainder = max_weight
        items = []
        overall_weigth, overall_value = 0, 0
        for item in combination:
            remainder = remainder - item[1]
            if remainder >= 0:
                overall_value += item[0]
                overall_weigth += item[1]
                items.append(item)
        ratio = overall_value / max_weight
        if ratio > best_ratio:
            best_ratio = ratio
            best_choice = items, (overall_value, overall_weigth, ratio)
    print('best_value is ' + str(best_choice[1][0]) + '\n')
    print('best_weigth is ' + str(best_choice[1][1]) + '\n')
    print('best_ratio (value/max weight of knapsack) is ' + str(best_ratio) +
          '\n')

    return 'best_choice is ' + str(best_choice[0]) + '\n'

# Measuring the time of execution
start = time.time()
print(best_choice_for_knapsack(items, knapsack))
end = time.time()
print('time of execution is ' + str(end - start))