# Create an algorithm that filters a list out of duplicates AND sorts the result.

def filterDuplicates(lst):
    lst = list(set(lst)) # converting to a set o(n) // converting to a list o(n) too 
                         # since this operation runs once it's just o(n) 
    return sorted(lst)   # sorted() uses merge sort so n log n

example = [10,10,10,2,2,2,3,3,3,3,1,1,1,9,100,1,-1]
example_filtered = filterDuplicates(example)

print(f"The result is: {example_filtered}")