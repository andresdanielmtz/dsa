'''
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
'''

# lc 1768
def mergeStrings(str1, str2):
    i = 0 # initial index
    res = []
    while (i <= len(str1) - 1 and i <= len(str2) - 1 ):
        if (str1[i]):
            res.append(str1[i])
        if (str2[i]):
            res.append(str2[i])
        i += 1
        
    if (i == len(str1) and i == len(str2)):
        return ''.join(res)
       
    if (i == len(str1)):
        res.append(str2[i:])
    elif (i == len(str2)):
        res.append(str1[i:])
     
    return ''.join(res)
    
word1 = ""
word2 = "pqr"
res = mergeStrings(word1, word2)
print(res)