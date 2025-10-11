# function that determines whetoer or not a list contains duplicates

def hasDuplicate(nums: list[int]) -> bool: 
    count = {} # because of this, space complexity = o(n)
    for num in nums: # o(n)
        if num not in count: # o(1) 
            count[num] = 0 # o(1)
        else:
            return True
    return False