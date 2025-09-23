from logger_config import logger

# this is for knowing the difference between parameterized and functional recursion 

logger.info("parameterized Recursion")
def sum_param(n, acc= 0):
    if n == 0:
        return acc
    
    return sum_param(n-1, acc+n)

print(sum_param(6))


logger.info("Functional Recursion")
# sum of n 
def sum_func(n):
    if n== 0:
        return 0
    return n + sum_func(n-1)

print(sum_func(6))


#  factorial of n 
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(3)) 
# TC = O(n)
# SC = O(n) stack space


logger.info("reverse a list")
# reverse a list 
a = [1,2,3,4,5,6,7]
b = []

def reverse(a):
    if len(a) == 1:
        return b.append(a[0])
    b.append(a[-1])
    return reverse(a[:-1])

print(reverse(a))
print(b)




