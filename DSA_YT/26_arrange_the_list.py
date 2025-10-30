from logger_config import logger

# logger.info("the question is to rearrange the list into positive and negative number ")

# def rearrange(lst):
#     post_list = []
#     neg_list = []
#     for i in lst:
#         if i > 0:
#             post_list.append(i)
#         else:
#             neg_list.append(i)
    
#     arrange_list = []
#     for i in range(len(lst)//2):
#         arrange_list.append(post_list[i])
#         arrange_list.append(neg_list[i])
    
#     return arrange_list
    
# print(rearrange([1,3,54,-4,-7,-12]))


# logger.info("optimal solution")
# def rearrange(lst):
#     arranged_list = len(lst)*[0]
#     p = 0
#     n = 1
#     for i in lst:
#         if i > 0:
#             arranged_list[p] = i
#             p+=2
#         else:
#             arranged_list[n] = i
#             n+=2
#     return arranged_list
    
# print(rearrange([1,3,54,-4,-7,-12]))

logger.info(f"{'='*50}")
logger.info("Longest sequence in number ")
data = [1,2,3,98,99,100,101]
def longest_seq(lst):
    sets = sorted(lst)
    lone_seq = 0
    temp_seq = 1
    for i in range(len(sets)-1):
        if (sets[i+1] - sets[i]) == 1:
            temp_seq +=1
        else:
            lone_seq = max(lone_seq, temp_seq)
            temp_seq = 1
    return max(lone_seq, temp_seq)

print(longest_seq(data))
