#ask the user about the weather
weather = input("What's the weather like today? (sunny, rainy, cold) ")
# provide advice based on the weather
if weather == "sunny":
    print("wear a t-shirt and sunglasses!")
elif weather == "rainy":
    print("dont forget your umbrella and raincoat.")
elif weather == "cold":
    print("make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have advice for that this weather.")