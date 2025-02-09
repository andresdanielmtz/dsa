height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def highest_body_water(height) -> int:
    l = 0
    r = len(height) - 1
    highest = 0

    while l != r:
        body = (r - l) * min(height[l], height[r])
        highest = max(highest, body)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return highest
        

res = highest_body_water(height)
print(res)