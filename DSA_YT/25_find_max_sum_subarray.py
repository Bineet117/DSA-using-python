from logger_config import logger
from typing import List

def max_sum(lst):
    max_num = 0
    for i in range(len(lst)):
        each_step_add = 0
        for j in range(i, len(lst)):
            each_step_add = each_step_add + lst[j]
            max_num = max(max_num, each_step_add)
    return max_num


print(max_sum([1,-5,8,-1]))

# stock buy and sell 
# buy and sell the stock at price where the profit is max
prices  = [7,2,1,5,6,4,8]
def max_pro(lst: List[int]) -> int:
    max_diff = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            diff = lst[j] - lst[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_pro(prices))