#simple calcualtor with match case

def main():
    #prompt the user to input a number

    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    
    #prompt the user to input the operation they would likke to use
    operation = input("Enter operation of choice (+, -, *, /):")
    #formulate a match case statement

     match operation:
        #matching case statement
          case '+':
                result = num1 + num2
                print("The result is {result}.")
          case '-':
                result = num1 - num2
                print("The result is {result}.")
            case '*':
                result = num1 * num2
                print("The result is {result}.")
            case '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print("The result is {result}.")
    #print result 
        result()
        Print("The result is:" , result)

if __name__ == "__main__":
    main()

