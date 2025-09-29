from logger_config import logger


logger.info("simple")
a = "bob"
b = a[::-1]
if a == b:
    print("true boss")


logger.info("brute loop")
a = "bob"
c = ""
for i in a[::-1]:
    c = c + i 
if a == c:
    print("true boss") 



logger.info("Recursion")
a = "bobs"
d = ""
def palin(a):
    if len(a) == 0:
        return
    
    d = d + a[-1]
    palin(a[:-1])

if a == c:
    print("true boss") 
else:
    print("bhaak")

# TC: O(len(a))  stack space
# SC: O(len(a))  



logger.info("Optimized Recursion")
a = "bob"
l = 0
r = len(a) - 1
def palin(a, l , r ):
    if l >= r:
        return "palindrome"
    
    if a[l] != a[r]:
        return "not palindrome"
    
    return palin(a , l+1, r-1)

print(palin(a, l, r))
# TC: O(len(a/2))  
# SC: O(len(a/2))  stack space