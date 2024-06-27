#prompt user to enter the following
rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
symbol = input("Enter symbol to use:")

# using the loops
while x in range (rows):
    while y in range (columns):
        print(symbol, end='')
    print()

