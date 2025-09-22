from logger_config import logger

logger.info("taking input")
n = int(input("give me some input: "))


def head_recursion(n):
    if n == 0:
        return 
    head_recursion(n-1)
    print(n)

head_recursion(n)
logger.info("-----------------------------------------")

def tail_recursion(n):
    if n == 0:
        return 
    print(n)
    tail_recursion(n-1)

tail_recursion(n)