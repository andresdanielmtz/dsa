def hasDuplicate(nums: list[int]):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        else:
            return True
    return False
