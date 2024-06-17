def maxDepth(s: str) -> int: 
    stack = []
    closing = ")"
    starting = "("
    counter = 0 
    for char in maxDepth:
        if char in starting: stack.append(char)
        elif stack and char in closing: stack.pop()
        if len(stack) > counter: counter = len(stack)
    return counter


