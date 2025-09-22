from logger_config import logging

lt = [1,1,1,1,2,2,2,3,3,3,3,3]

a = {

}
st = list(set(lt))
print(st)

logging.info("Brute force")
for i in st:
    k = 0
    for j in lt:
        if(j == i):
            a[i] = k
            k = k + 1
            a[i] = k
    # a[i] = k
print(a)


logging.info("better way")
lt = [1,1,1,1,2,2,2,3,3,3,3,3]
a = {
}
for i in lt:
    if i in a:
        a[i] = a[i] + 1
    else:
        a[i] = 1

print(a)

logging.info("optimized way")
lt = [1,1,1,1,2,2,2,3,3,3,3,3]
a = {
}
for i in lt:
    if a.get(i,0) != 0:
        # print(a[i])
        a[i] = a[i] + 1
    else:
        a[i] = 1
print(a) 