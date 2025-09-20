
from logger_config import logger


logger.debug("First way of doing it")
a = 3456789
for i in str(a):
    print(i)

logger.info("second way of doing it by convertint to string and reversing it")
a = 3456789
for i in str(a)[::-1]:
    print(i)

logger.debug("Second way of doing it")
a = 3456789
while a > 0:
    print(a%10)
    a = a//10

