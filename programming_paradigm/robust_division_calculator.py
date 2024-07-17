def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator 


        print(f"The result of the division is {result}")

          
    except ZeroDivisionError:
        return"Error: Cannot divide by zero."

    except ValueError:
        return"Error: Please enter numeric values only."

    except Exception as e:
        print(f"Unexpected error occured: {str(e)}")
    return f"The result of the division is {result:1f}"



            


