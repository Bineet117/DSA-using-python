from logger_config import logger
from typing import List

logger.info("using while loop")
def binary_search(arr: List[int], tar:int) -> int:
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            high = mid - 1
        else:
            low = mid +1
    return -1

print(binary_search([1,2,4,5,6,8,9], 8))

logger.info("using recursion")
def binary_search(arr: List[int], low:int, high:int, tar:int) -> int:
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_search(arr, low, mid-1, tar)
    else:
        return binary_search(arr, low+1, high, tar)

print(binary_search([1,2,4,5,6,8,9], 0, 6, 8))