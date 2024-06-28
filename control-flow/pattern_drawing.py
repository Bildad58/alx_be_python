#prompt user to enter the following
size = input("Enter size of pattern:")
rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
symbol = input("Enter symbol to use:")
size == rows
# using the loops
for x in range (rows):
    for y in range (columns):
        print(symbol, end='')
    print()

