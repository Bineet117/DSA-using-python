from logger_config import logger
from typing import List

logger.info("Removing duplicate element from sorted list")

lt = [1,1,1,2,3,4,5,6,6,7,7,7]

logger.info("brute")
def duplicate(data: List[int]) -> List[int]:
    sets = list(set(data))
    data[:len(sets)] = sets
    return data

# print(duplicate(lt))


logger.info("")
def duplicate(data: List[int]) -> List[int]:
    ll = []
    d = {}
    for i in data:
        if i not in d:
            d[i] = 0
            ll.append(i)
    
    data[:len(ll)] = ll[:]
    return data
        
print(duplicate(lt))
