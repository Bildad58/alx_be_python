def perform_operation(num1, num2, operation ):
   
   match operation:
      case'add':
         result = num1 + num2 
      case 'subtract':
         result = num1 - num2 
      case 'multiply':
         result = num1 * num2 
      case 'divide':
         result = num1 / num2
         if num1 / 0:
            print("Please enter a whole number")
      case _ :
         print("Invalid mathematical operation")
        
   
perform_operation('num1', 'num2', 'operation')
