import time #線性搜尋法
import random
sTime=0
r = random.randrange(0,100000001)
def linearSearch():
    sTime=time.time()
    for i in range(100000001):
        if 100000000==i:
            print(time.time()-sTime)
            break
linearSearch()
