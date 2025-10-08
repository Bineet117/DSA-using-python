from logger_config import logger 

data = [34, 21, 9, 0, 2, 95, 5, 7, 11]

logger.info("Largest number")
def largest_num(arr):
    max = arr[0] 
    for i in data:
        if i > max:
            max = i

    return max
    
print(largest_num(data))

logger.info("Largest number using while loop")
def largest_num(arr):
    max = arr[0] 
    i = 0
    while i < len(arr):
        if arr[i] > max:
            max = arr[i]
        i += 1
    return max
    
print(largest_num(data))


# Find Second largest number 
logger.info("Find second Largest number {brute}")
data = [34, 21, 9, 0, 2, 95, 5, 7, 11]
def second_lar(arr):
    return sorted(arr)[-2]

print(second_lar(data))


logger.info("Find second Largest number {better}")
data = [34, 21, 9, 0, 2, 95, 5, 7, 11]
def second_lar(arr):
    # bubble sort
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[-2]

print(second_lar(data))

logger.info("Find second Largest number {optimal}")
def second_lar(arr):
    largest = float("-inf")
    sec_largest = float("-inf")
    for i in arr:
        if i > largest:
            sec_largest = largest
            largest = i
        elif i > sec_largest and i != largest:
            sec_largest = i
    return sec_largest

data = [34, 5, 8]
print(second_lar(data))



