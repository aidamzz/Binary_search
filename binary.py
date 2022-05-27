#looking through all and each data, not good for large amount of data
def liner_search(data, target):
    for i in data:
        if i == target:
            return True
    return False

#more efficent way
def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1
    
    while low <= high:
        mid = (high + low)//2
        if target == data[mid]:
            return True
            
        elif target > data[mid]:
            low = mid +1
        else:
            high = mid -1
    return False

#without loop
def binary_search_withoutloop(data, target, low, high):
    if low >high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        else:
            if target > data[mid]:
                return binary_search_withoutloop(data, target, mid+1, high)
            else:
                return binary_search_withoutloop(data, target, low, mid-1)