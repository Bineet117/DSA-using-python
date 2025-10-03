from logger_config import logger
from typing import List


logger.info("Ascending order")
nums = [3,4,2,6,1,8,9,34]
def bubble(nums : List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(0, len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

print(bubble(nums))


logger.info("Descending order")
nums = [3,4,2,6,1,8,9,34]
def bubble(nums : List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(0, len(nums)-1-i):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

print(bubble(nums))