nums = [1, 1, 2, 2, 3]


# boyer-moore majority vote system
def majorityElement(nums):
    counter = 0
    majority = 0
    for num in nums:
        if counter == 0:
            majority = num
            counter = 1
        elif majority == num:
            counter += 1
        else:
            counter -= 1
    return majority


res = majorityElement(nums)
print(f"result: {res}")
