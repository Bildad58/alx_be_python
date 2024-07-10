def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator 
          
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except ValueError:
        print("Error: Please enter numeric values only.")
    
    else:
        print(f"The result of division is {result}")

numerator = float(input("Enter a number: "))
denominator = float(input("Enter a number: "))

safe_divide(numerator,denominator)