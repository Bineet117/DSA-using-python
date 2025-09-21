lt = [1,1,1,1,2,2,2,3,3,3,3,3]

a = {

}
st = list(set(lt))
print(st)

for i in st:
    k = 0
    for j in lt:
        if(j == i):
            a[i] = k
            k = k + 1
            a[i] = k
    # a[i] = k
print(a)
