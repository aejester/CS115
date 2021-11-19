import time

test_list = list(range(0, 1000000000))

def linear(l: list[int], key: int) -> int:
    for i in range(len(l)):
        if l[i] == key:
            return i
    return -1

def binary(l: list[int], key: int) -> int:
    low = 0
    high = len(l) - 1
    while low <= high:
        middle = low + (high - low) // 2
        print(middle)
        if l[middle] == key:
            return middle
        elif l[middle] < key:
            low = middle
        elif l[middle] > key:
            high = middle
    return -1

KEY = 567890
    
l_start = time.time()
l_res= linear(test_list, KEY)
print(str(l_res)+" in "+str((time.time() - l_start) * 1000)+"s")

b_start = time.time()
b_res = binary(test_list, KEY)
print(str(b_res)+" in "+str((time.time() - b_start) * 1000)+"s")