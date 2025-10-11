
# builtin 

builtin_arr = list(reversed(range(1, 10))) # 9 to 0
print(builtin_arr[::-1])

# in place sol 
def reverseArray(arr): 
    l, r = 0, len(arr) - 1
    while l!=r:
        aux = arr[l]
        arr[l] = arr[r]
        arr[r] = aux
        l += 1 
        r -= 1  
    return arr 

arr = [9,8,7,6,5,4,3,2,1]
reverse_arr = reverseArray(arr) 
print(reverse_arr)

# new list (naive due to requiring extra memory) 

def reverseArrayWithNewList(arr):
    newList = [] 
    for elem in arr: 
         newList.insert(0, elem)
    return newList

newList_example = list(reversed(range(1, 10))) # 0 to 9  
reverse_newList_example = reverseArrayWithNewList(newList_example)

print(reverse_newList_example)