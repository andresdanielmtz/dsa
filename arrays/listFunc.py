topTenReverse = reversed(range(0,10))
print(topTenReverse) # range_iterator object 
print(type(topTenReverse)) # class range_iterator 
print(list(topTenReverse)) # 9 .. 0 

# list() is important in order to have a place in memory where to iterate -> an object. 