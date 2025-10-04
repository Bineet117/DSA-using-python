from logger_config import logger

nums = [3,4,2,6,1,8,9,34]

for i in range(len(nums)):
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[i]:
            min_index = j
    nums[i], nums[min_index] =  nums[min_index], nums[i]

print(nums)


logger.info("descending order")
nums = [3,4,2,6,1,8,9,34]

for i in range(len(nums)):
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            min_index = j
    nums[i], nums[min_index] =  nums[min_index], nums[i]

print(nums)