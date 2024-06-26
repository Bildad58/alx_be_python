#weatheradvice
#prompt user to input current weather.
Weather = input("What's the Weather like today? (sunny/rainy/cold): ")

#provide proper clothing recomendation based on weather.
if Weather == "sunny" :
    print("Wear a t-shirt and sunglasses.")
elif Weather == "rainy" :
     print("Don't forget your umbrella and a raincoat.")  
elif Weather == "cold" :
     print("Make sure to wear a warm coat and a scar")      
else :
     print("Sorry, I don't have recommendations for this weather")  
    

