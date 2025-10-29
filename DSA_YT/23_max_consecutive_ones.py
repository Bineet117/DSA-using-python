data = [1,1,0,0,1,1,1,1,0,0]
def consecutive(lt):
    counter = 0
    max_ones = 0
    for i in lt:
        if i == 1:
            counter+=1
        else:
            max_ones = max(max_ones, counter)
            counter = 0
    return max(max_ones, counter)

print(consecutive(data))  
    
# TC: O(n)
# SC: O(1)