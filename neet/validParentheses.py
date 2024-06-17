def isValid(s: str) -> bool: 
    stack = [] 
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    for char in s: 
        # if char not in closeToOpen: return False # ??
        if char in closeToOpen.keys() and len(stack) == 0: return False
        if char in closeToOpen.values(): 
            stack.append(char)
        if char in closeToOpen.keys() and stack[-1] == closeToOpen[char]: 
            stack.pop() 
    return len(stack) == 0 


string = "]"
res = isValid(string)
print(res)

