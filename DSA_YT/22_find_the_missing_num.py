from logger_config import logger 

lt = [1,0,2,4]


def missing(lt):
    lt = set(lt)
    for i in range(len(lt) +1):
        if i not in lt:
            return i
    return -1

print(missing(lt))