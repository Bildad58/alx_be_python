<<<<<<< HEAD
x =" hello "
strip(x)
=======
# weather_advice.py

def main():
    # Prompt the user for the current weather
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
    
    # Provide clothing recommendations based on the weather input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    main()


>>>>>>> 95d19eb34c98901e80e832c436b4cff7d4b132d2
