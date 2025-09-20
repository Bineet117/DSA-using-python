from logger_config import logger

logger.info("palindrome code using string conversion")
a = 121
rev = int(str(a)[::-1])
if a == rev:
    print("True")
else:
    print("false")



logger.info("second way")
a = 121
num = a
b = 0
while a > 0:
    b = b*10 + (a%10)
    print(b)
    a = a//10

if b == num:
    print("True")
else:
    print("false")