"""
2. given an integer, if 2 adjecent digit are both odd or even, we can do a swap for these digit.
Like for 597683
swap 5 and 9 -> 957683
swap 5 and 7 -> 975683
swap 6 and 8 -> 975863
"""

example_num = 597683
example_num = [int(x) for x in str(example_num)]
print(example_num)


def getPattern(x: int, y: int) -> bool:
    if (x % 2 == 0) and (y % 2 == 0) or (x % 2 == 1) and (y % 2 == 1): 
        return True
    return False


for i in range(0, len(example_num) - 1):
    print(example_num)
    pattern = getPattern(example_num[i], example_num[i + 1])
    if pattern:
        temp = example_num[i]
        example_num[i] = example_num[i + 1]
        example_num[i + 1] = temp
