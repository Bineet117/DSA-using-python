from logger_config import logger


a = [2,8,15,18]
b = [5,9,12,17]

def merge_sorted_array(arr1 , arr2):
    c = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            c.append(arr1[i])
            i = i+1
        else:
            c.append(arr2[j])
            j = j+1
    
    c.extend(arr1[i:])
    c.extend(arr2[j:])

    return c

# print(merge_sorted_array(a,b))

def merge_sort(ar):
    if len(ar) == 1:
        return ar
    
    arr = len(ar)//2
    left = merge_sort(ar[:arr])
    right = merge_sort(ar[arr:])

    return merge_sorted_array(left, right)

print(merge_sort([34,21,9,0,2,4,5,7,11]))