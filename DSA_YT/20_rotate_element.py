from logger_config import logger
from typing import List 

logger.info("Rotate element by k place")

data = [2,3,4,5,6,7,1]
logger.info("Right rotate element by 1 place")
def rotate(data: List[int], k: int) -> List[int]:
    a = 0
    while a < k:
        element = data[-1]
        for i in range(len(data)-1, 0 , -1):
            data[i] = data[i-1]
        data[0] = element
        a+=1
    return data

print(rotate(data, 2))

data = [2,3,4,5,6,7,1]
logger.info("Right rotate element by k place")
def rotate(data: List[int], k: int) -> List[int]:
    n = len(data)
    for i in range(k):
        element = data[n-1]
        data[:] = [element] + data[:n-1]
    return data

print(rotate(data, 2))


logger.debug("===========================")
logger.debug("===========================")
logger.debug("===========================")
logger.debug("===========================")
logger.debug("===========================")

logger.info("Move zeroes ot the end")
data = [2,3,4,0,5,6,0,7,1]
def move_zeroes(data):
    non_zeroes = [i for i in data if i != 0]
    zeroes = [0] * (len(data) - len(non_zeroes))
    data[:] = non_zeroes + zeroes
    return data

print(move_zeroes(data))