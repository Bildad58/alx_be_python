def perform_operation(num1 , num2, operation):
    if operation =='add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation =='multiply':
        return num1 * num2 
    elif operation == 'divide':
        if num2 ==  0:
         print("Enter a whole number")
        else:
         return num1 / num2 
    else:
       print("Invalid number and operation")

       
perform_operation()
    

