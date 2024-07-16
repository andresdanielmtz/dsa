arr = [1]

def valSameAsIndex(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] == i + 1:
            res.append(i + 1)
    return res

res = valSameAsIndex(arr)
print(res)
