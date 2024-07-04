def perform_operation(num1, num2, operation):
    if operation =='add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation =='multiply':
        return num1 * num2 
    
    elif operation == 'divide':
<<<<<<< HEAD
         return num1 / num2 
    if num2 / ==  0:
         print("Enter a whole number")
    else:
       print("Invalid number and operation:")

num1 = float(input("Enter number of choice:"))
num2 = float(input("Enter number of choice:"))
operation =input("Enter operation operator of choice:")

perform_operation(num1, num2, operation)
=======
        if num2 ==  0:
         print("Enter a whole number")
        else:
         return num1 / num2 
    else:
       print("Invalid number and operation:")

num1 = float(input("Enter number of choice:"))
num2 = float(input("Enter number of choice:"))
operation =input("Enter operation operator of choice:")

perform_operation(num1, num2, operation)

>>>>>>> eab572d7b3d46753448805d098cfa99e68068a93
