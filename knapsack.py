""" Knapsack problem https://en.wikipedia.org/wiki/Knapsack_problem
(Best choice of items for knapsack in 0-1 Knapsack Problem) """

from itertools import permutations
import time

knapsack = 15
# Items
# value weight
# 1      14
# 13     11
# 6      7
# 9      10
# 3      3
# 2      7
# 4      10
# 7      6
# 5      5
items = {
    1: 14,
    13: 11,
    6: 7,
    9: 10,
    3: 3,
    2: 7,
    4: 10,
    7: 6,
    5: 5
}
def best_choice_for_knapsack(d, kp):
    combinations = permutations(list(d.items()), len(d))
    best_choice = []
    best_ratio = 0
    for combination in combinations:
        remainder = kp
        items = []
        overall_weigth, overall_value = 0, 0
        for item in combination:
            remainder = remainder - item[1]
            if remainder >= 0:
                overall_value += item[0]
                overall_weigth += item[1]
                items.append(item)
        ratio = overall_value / kp
        if ratio > best_ratio:
            best_ratio = ratio
            best_choice = items, (overall_value, overall_weigth, ratio)
    print('best_value is ' + str(best_choice[1][0]) + '\n')
    print('best_weigth is ' + str(best_choice[1][1]) + '\n')
    print('best_ratio (value/max weight of knapsack) is ' + str(best_ratio) +
          '\n')

    return 'best_choice is ' + str(best_choice[0]) + '\n'

start = time.time()
print(best_choice_for_knapsack(items, knapsack))
end = time.time()
print('time of execution is ' + str(end - start))

