from logger_config import logger

num = [1,2,4,4,4,5,6]
num2= [1,3,5,9]

def sorted(num, num2):
    lt = []
    i = j = 0
    while i < len(num) and j < len(num2):
        if num[i] > num2[j]:
            lt.append(num2[j])
            j = j+1
        else:
            lt.append(num[i])
            i =i+1
    lt.extend(num[i:])
    lt.extend(num2[j:])

    return list(set(lt))

print(sorted(num, num2))

    
    