from logger_config import logger
from typing import List

data = [3,4,2,6,1,8,9,34]

def insertion_sort(arr):
    for i in range(1, len(arr)):       # start from 2nd element
        num = arr[i]                   # number to insert
        j = i - 1
        while j >= 0 and arr[j] > num: # shift bigger numbers right
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num                 # place the number
    return arr

print(insertion_sort([4,3,1,2]))



def insert(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        a = arr[i]
        j = i-1
        while j>=0 and arr[j] > a:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = a
    return arr

print(insert(data))












