sTime=0
import time
def BinarySearch():
    low=-1
    upper=100000001
    sTime=time.time()
    while low<=upper:
        mid=(low+upper)//2
        if mid<99999999:
            low=mid+1
            print("big")
        elif mid>99999999:
            upper=mid-1
            print("small")
        else:
            print(time.time()-sTime)
            break
BinarySearch()