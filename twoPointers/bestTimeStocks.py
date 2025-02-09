"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

# two pointer
# left has to be the lowest
# right has to be the highest

prices = [2,1,2,1,0,1,2]



def get_max_stock(prices):
    l = 0
    r = 1

    lowest = float("inf")
    highest = float("-inf")

    gap = 1
    while (r - l) != len(prices):

        if prices[l] < lowest and prices[l] != highest:
            lowest = prices[l]
        if prices[r] > highest and prices[r] != lowest:
            highest = prices[r]

        l += 1
        r += 1
        if r >= len(prices):  # return to origin and expand gap by 1
            l = 0
            gap += 1
            r = gap

    total = highest - lowest
    return 0 if total < 0 else total

def for_n(prices):
    lowest = [float('inf'),-1]
    highest = [float('-inf'),len(prices)]

    for i in range(0, len(prices)):
        if prices[i] < lowest[0] and i < highest[1]:
            lowest[0] = prices[i]
            lowest[1] = i
        if prices[i] > highest[0] and i > lowest[1]:
            highest[0] = prices[i]
            highest[1] = i
    
    print(f"Index: {highest[1]} && {lowest[1]} ")
    total = highest[0] - lowest[0]
    return (0 if total < 0 else total)

res_two = for_n(prices)
print(f"result (2): {res_two}")
