s = "aa"

def lengthLastWord(string: str) -> int: 
    r = len(string) - 1
    word_length = 0
    while string[r] == " " and r>= 0: # to avoid taking the length of whitespace
        r -= 1 
    
    # we count how many times does it appear + that it maintains in bounds (no smaller than 0 which is the smallest possible index)
    while string[r] != " " and r >= 0:
        print(f"second loop called \t r={r}")
        word_length += 1
        r -= 1 
    
    return word_length
    
lengthLastWord(s) 