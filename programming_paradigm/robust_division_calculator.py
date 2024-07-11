def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator 
<<<<<<< HEAD
        print(f"The result of division is {result}")
=======

        print(f"The result of the division is {result}")
>>>>>>> d719e5aa806d276bcf17a3a01c6de86d42d2e538
          
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter numeric values only.")
    
<<<<<<< HEAD
    
       
safe_divide(90,0)
=======
safe_divide(90,15)
>>>>>>> d719e5aa806d276bcf17a3a01c6de86d42d2e538
