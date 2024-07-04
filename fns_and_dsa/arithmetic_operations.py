def perform_operation(num1, num2, operation ):
   
   if operation == 'add':
      result = num1 + num2
   elif operation == 'divide':
      if num1 / 0:
         print("Please enter a whole number")
      result = num1 / num2
   elif operation == '*':
      result == num1 * num2
   elif operation == '-':
      result = num1 - num2
   else:
      print("Invalid number and opreation")

perform_operation()
