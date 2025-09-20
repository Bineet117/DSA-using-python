from logger_config import logger
import math

a = 3456797986

logger.info("This is first way")

count = 0
for i in str(a):
    count = count +1 
print("The number of digits in the number is:", count)
logger.info(f"Loop ends here ")


logger.info("----")
logger.info("----")
logger.info(20*"-")
logger.info(20*"-")
logger.info("----")
logger.info("----")

logger.info("This is Second way")
b = 0
while a > 0:
    a = a//10
    b = b+1

print(f"the count is {b}")
logger.info(f"Loop ends here ")

logger.info("----")
logger.info("----")
logger.info(20*"-")
logger.info(20*"-")
logger.info("----")
logger.info("----")

logger.info("This is third way")
a = 3456797986
print(int(math.log10(a)) + 1)