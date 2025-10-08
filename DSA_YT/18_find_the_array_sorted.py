from logger_config import logger

data = [34, 21, 9, 0, 2, 95, 5, 7, 11]

data1 = [1,2,3,4,5,1]


def sorted_list(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
            return sorted
    return sorted
print(sorted_list(data1))
