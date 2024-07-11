def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

<<<<<<< HEAD
        result = numerator / denominator
=======
        result = numerator / denominator 

>>>>>>> 5a6e5e5e12d16d197f56244a4d9fb87599599f68

        print(f"The result of the division is {result}")

          
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
<<<<<<< HEAD
        print("Error: Please enter numeric values only.")
    

=======
        print("Error: Please enter numeric values only."
               
>>>>>>> 5a6e5e5e12d16d197f56244a4d9fb87599599f68
safe_divide(90,15)

