from logger_config import logger

n = 15
logger.info("Using for loop")
for i in range(1,n+1):
    if n%i == 0:
        print(i)


logger.info("Using while loop")
i = 1
while i <= 15:
    if n % i == 0:
        print(i)
    i += 1