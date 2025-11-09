from logger_config import logger

logger.info("Leetcode 35")
logger.info("search insert position:")

def find_insert_position(data, target):
    lb = len(data)
    low = 0
    high = len(data)
    while high >= low:
        mid = (high + low)//2
        if data[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb


print(find_insert_position([1,2,4,5,6,8,9], 2))


logger.info("CEIL the FLOOR")
def ceil_the_floor(data, target):

    high = len(data)
    low = 0
    while high >= low:
        mid = (low+high)//2
        if data[mid] == target and mid == 0:
            return [-1, target]
        elif data[mid] == target and mid == len(data)-1:
            return [target, -1]
        elif data[mid] == target:
            return [target, target]
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

print(ceil_the_floor([1,2,4,5,6,8,9], 3))