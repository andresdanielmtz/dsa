# function that determines whetoer or not a list contains duplicates

def hasDuplicate(nums: list[int]) -> bool: 
    count = {}
    for num in nums: # o(n)
        if num not in count: # o(1) 
            count[num] = 0 # o(1)
        else:
            return True
    return False