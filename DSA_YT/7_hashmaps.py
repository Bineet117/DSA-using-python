from logger_config import logger

'''
constraints:
- 
'''

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

a = {}
for i in n:
    if i in a:
        a[i] = a[i]+1
    else:
        a[i] = 1

for i in m:
    if i in a:
        print(i, ":", a[i])


logger.info("character hashing")

# count character
a = "ysdtrytfuyigursdytfkghurtfgyjhkjrtdtfg"

d = {}

for i in a:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1

print(d)

