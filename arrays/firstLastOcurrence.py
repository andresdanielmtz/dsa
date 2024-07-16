arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
target = 7
"""
if num == target and first == 0: 
            first = 

"""


# O ( n ^ 2 )
def firstAndLastOcurrence(arr, target):
    first, last = 0, 0
    for i in range(len(arr)):
        if arr[i] == target:
            if first == 0:
                first = i
                last = i
            else:
                last = i
    if first:
        return [first, last]
    else:
        return []


res = firstAndLastOcurrence(arr, target)
print(res)


def firstLast(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        if arr[l] == arr[r] and arr[l] == target:
            return [l, r]
        if arr[r] > target:
            r -= 1
        elif arr[l] < target:
            l += 1
    return [-1, -1]


res2 = firstLast(arr, target)
print(res2)
