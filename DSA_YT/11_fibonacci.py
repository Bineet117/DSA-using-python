from logger_config import logger

# fibonacci
# 0,1,1,2,3,5,8,13,21.....

logger.info("brute force")
k = 8
def fibo(a= 0, b=1 , n = 2):
    if n == k:
        return b
    
    c = a+b
    a,b = b,c
    return fibo(a,b,n+1)

print(fibo())

# TC = O(k-2)
# SC = O(k-2) stack space

logger.info("Optimized")
def fibo(n):
    if n == 0 or n == 1:
        return n
    
    return fibo(n-1) + fibo(n-2)

print(fibo(3))
    

