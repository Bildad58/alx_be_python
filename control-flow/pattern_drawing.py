<<<<<<< HEAD
# prompt the use to input size of pattern
size = int(input("Enter size of pattern:"))

# begin count of row
row = 0

# iterate through each row
while row<size:
    #print the asterisks
    for _ in range (4):
     #print new line
     print("*" , end='')
    row += 1
=======
#prompt user to enter the following
size = int(input("Enter size of pattern:"))
rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
symbol = input("Enter symbol to use:")
size == rows
# using the loops
for x in range (rows):
    for y in range (columns):
        print(symbol, end='')
>>>>>>> 0dd36fee532f7c0ccc30cd161fc661f861395b23
    print()
~
