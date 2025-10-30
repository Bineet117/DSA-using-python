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
