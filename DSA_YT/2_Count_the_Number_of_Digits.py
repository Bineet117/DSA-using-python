a = 3456797986

count = 0
for i in str(a):
    count = count +1 
print("The number of digits in the number is:", count)


b = 0
while a > 0:
    a = a//10
    b = b+1

print(f"the count is {b}")