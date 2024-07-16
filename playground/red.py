# 2 people A and B have same length of array all contains int, and with a startFlag odd and even. what you need to do is to calculate the sum of arrayA-arrayB of each odd item or even item (based on startFlag). if sum >0, A wins, output A's name, if sum<0, output B's name, if sum==0, output Tie
# like:
# Tom=[2,2,3]
# Jerry=[3,1,4]
# flag=odd
# sum = (2-3)+(3-4)=-2

tom = [2, 2, 3]
jerry = [3, 1, 4]
flag = "odd" # indexes 1, 3, 5 but 1 = first element 

total = 0
starting_position = 0 
if flag == "even": starting_position += 1 

for i in range(starting_position, len(tom), 2):
    total += tom[i] - jerry[i]

print(total)
if total > 0: print("Tom")
elif total < 0: print("Jerry")
else: print("Tie")

