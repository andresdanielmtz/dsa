# Usually there's two uses for the two pointer

# Fast and Slow pointer
# Pointer that starts from the left and pointer that starts from the right

# N Log(N) > N^2
# Use Cases:
# - Sort and scan array
# - Scan through array and use binary search

# If Array is sorted, one should look into binary search.

# Problem:
# Given an array of sorted integers, find two numbers such that they add up to a target number.

arr = [1, 2, 3, 4, 5, 6, 7]
target = 9


def getSumIndexes(arr, target):
    back, front = 0, len(arr) - 1
    while back < front:
        total = arr[back] + arr[front]
        if total > target:
            front -= 1
        elif total < target:
            back += 1
        else:
            return [back, front]
    return []


res = getSumIndexes(arr, target)
print(res)

"""
while (arr[back] + arr[front]) != target:
    if arr[back] + arr[front] > target:
        back += 1 
    elif arr[back] + arr[front] < target:
        front -= 1
    else:
        print([back, front])
"""
