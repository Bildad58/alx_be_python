# prompt the use to input size of pattern
size = int(input("Enter size of pattern:"))

# begin count of row
row = 0

# iterate through each row
while row<size:
    #print the asterisks
    for _ in range (size):
     #print new line
     print("*" , end='')
    row += 1
