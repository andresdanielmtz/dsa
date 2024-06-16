arbitrary_arr = [1,2,3,4,3,2,1,5,2,1,2,10,2,35,1,2]

def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i] 
                arr[i] = arr[j]
                arr[j] = temp
    return arr

print(f"Original Array: {arbitrary_arr}")
final_arr = bubble_sort(arbitrary_arr)
print(f"Final Array: {final_arr}")