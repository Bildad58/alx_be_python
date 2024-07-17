def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator 


        return f"The result of the division is {result}"

          
    except ZeroDivisionError:
<<<<<<< HEAD
        return"Error: Cannot divide by zero."

    except ValueError:
        return"Error: Please enter numeric values only."

    except Exception as e:
       return e
    



=======
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
        
    except Exception as e:
         return e


    
>>>>>>> a3911b3e0683f253cd3767dfb72ed9e5aa5fe7d8
            


