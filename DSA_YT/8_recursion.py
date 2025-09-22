from logger_config import logger

logger.info("taking input")
# n = int(input("give me some input: "))
n = 4

logger.info("--------------Head Recursion---------------------------")
def head_recursion(n):
    if n == 0:
        return 
    head_recursion(n-1)
    print(n)

# head_recursion(n)

logger.info("--------------Tail Recursion---------------------------")
def tail_recursion(n):
    if n == 0:
        return 
    print(n)
    tail_recursion(n-1)

# tail_recursion(n)


logger.info("--------------Recursion using parameters---------------------------")
# print x, n times
x = 89
n = 5
def printing_data(x,n):
    if n == 0:
        return
    print(x)
    printing_data(x, n-1)

# printing_data(x,n)

logger.info("--------------Printing 1 to n---------------------------")
n = 12
def print_num(n):
    if n == 0:
        return
    
    print_num(n-1)
    print(n)
# print_num(n)

n = 3
def print_nnnn(k,n):
    if k > n:
        return
    
    print(k)
    print_nnnn(k+1, n)

print_nnnn(1,n)