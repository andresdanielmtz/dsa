# lc 283
def moveZeroes(nums):
    # two pointer, have one in the beginning and other replacing the rest of elements 
    l, r = 0, 0
    while (l < len(nums) and r < len(nums)):
        if nums[r] != 0:
            nums[l] = nums[r]
            l += 1
        r += 1
    for i in range(l, len(nums)):
        nums[i] = 0    
    print(nums)

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)