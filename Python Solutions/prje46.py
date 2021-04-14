from time import time
from primeHelper import Prime


arr = Prime.genPrime(100,noBool = True)

def close(n:int) -> int:

    if n <= arr[0]: return arr[0]
    if n >= arr[len(arr) - 1]: return arr[len(arr) - 1]

    i = 0; j = len(arr); mid = 0
    while i < j:
        mid = (i + j) // 2

        if arr[mid] == n: return arr[mid]
        else:
            if n < arr[mid]:
                if mid > 0 and n > arr[mid - 1]:
                    v1 = arr[mid -1]; v2 = arr[mid]
                    if n - v1 > v2 - n: return v2
                    return v1
                
                j = mid
            else:
                if mid < len(arr) - 1 and n < arr[mid + 1]:
                    v1 = arr[mid]; v2 = arr[mid + 1]
                    if n - v1 > v2 - n: return v2
                    return v1

                i = mid + 1
    return arr[mid]
st = time()


# l = {}
# for i in range(35,1000,2):
#     pass


print(close(10))
print(f"Time taken : {time() - st}")
#Avg Time Taken:  seconds