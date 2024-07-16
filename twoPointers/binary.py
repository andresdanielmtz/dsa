from typing import List

arr = [1, 2, 3, 4]
target = 3

# O(log n) since on the worst case scenario the number to iterate get divided by 2. So Log_2  
def binary_search(arr, target): 
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2 # the midpoint, the // is to obtain the integer part of the division 
        if arr[mid] < target: # if the target is greater than the middle point 
            low = mid + 1
        elif arr[mid] > target: # if the target is lower than the middle point 
            high = mid - 1
        else:
            return mid 
    return -1

# Neetcode Search

def search(nums: List[int], target: int) -> int: 
    l, r = 0, len(nums) - 1

    while l <= r: 
       m = (l + r) // 2 # Might give us integer overflow, in that case we could use 
       m = 1 + ((r - l) // 2)

       if nums[m] > target:
           high = m - 1
       elif nums[m] < target:
            low = m + 1
       else: return m
    return -1
res = binary_search(arr, target)
print(res)
