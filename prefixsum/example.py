arr = [10, 20, 10, 5, 15]
print(arr)
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]
print(arr) # [1, 3, 6, 10, 15]
