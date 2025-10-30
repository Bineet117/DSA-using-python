from logger_config import logger

logger.info("brute force")

def two_sum(lst, num):
    for i in range(len(lst)):
        for j in range(0,len(lst)):
            if i == j:
                pass
            else:
                if ((lst[i] + lst[j]) == num):
                    return i,j
    return -1


print(two_sum([5,9,1,2,4,15,6,3], 13))

# TC: O(n)
# SC: O(n)


logger.info("optimal way ")

def two_sum(lst, num):
    dic = {}
    for i in range(len(lst)):
        remaining = num-lst[i]

        if remaining in dic:
            return i, dic[remaining]
        dic[lst[i]] = i
    return -1
    

print(two_sum([5,9,1,2,4,15,6,3], 13))

# TC: O(n) 
# SC: O(n)
