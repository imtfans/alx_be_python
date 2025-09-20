#ask the user about the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")
weather = weather.lower()
# provide advice based on the weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses!")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have advice for this weather.")

    
