def gcd(a, b):
    if a == 0: 
        return b  
    elif  b == 0:
        return a
         
    
    quotient = a // b 
    remainder = a % b
    a = (b * quotient) + remainder
    
    return gcd(b,remainder)

def gcd_common(a,b):
    if b == 0: return a 
    
    remainder = a % b
    return gcd_common(b, remainder); 

a = 270
b = 192
res = gcd(a,b)
res_common = gcd(a,b)

print(f"res: {res}")

print(f"res common: {res_common}")