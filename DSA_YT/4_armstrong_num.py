from logger_config import logger 


logger.info("Armstrong num")

logger.debug("starts here")
num = 153
back = num
check = 0
while num> 0:
    check = check + (num%10)**3
    print(check, num)
    num = num//10
    print(num)


if back == check:
    print("True")
else:
    print("false")