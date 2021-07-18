

# start of function 
def wind_chill(Temperature):
    # if you read this, let me know if it matters if I initialize a value or not
    wind_chill = 0
    
    user_input = input("Fahrenheit or Celsius (F/C)? ")

    if user_input.upper() == "F":

       for i in range(1,13):
            wind_mph = 5
            wind_mph = wind_mph * i
            wind_chill = 35.74 + (0.6215 * Temperature) - (35.75 * (wind_mph ** 0.16)) + (0.4275 * Temperature * (wind_mph ** 0.16))
            print(f"At temperature {Temperature:.1f}F, and wind speed {wind_mph} mph, the windchill is: {wind_chill:.2f}F")
    
    elif user_input.upper() == "C":
        Temperature = (Temperature * 9 / 5) + 32
        
        for i in range(1,13):
            wind_mph = 5
            wind_mph = wind_mph * i
            wind_chill = 35.74 + (0.6215 * Temperature) - (35.75 * (wind_mph ** 0.16)) + (0.4275 * Temperature * (wind_mph ** 0.16))
            print(f"At temperature {Temperature:.1f}F, and wind speed {wind_mph} mph, the windchill is: {wind_chill:.2f}F")


temperature = int(input("What is the temperature? "))

wind_chill(temperature)