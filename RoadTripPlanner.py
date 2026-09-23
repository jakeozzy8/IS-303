# Author: Jacob Osborne
# Create a program that asks user for name, 
# trip details,
# car details such as MPG, 
# and calculate pricing for trip

#INPUTS
first_name = input("Enter your first name: ").upper()
trip_destination = input("Where are you traveling? ")
trip_distance = float( input("How many miles away is your destination? "))
car_model = input("What model is your car? ")
miles_per_gallon = float( input("How many miles per gallon does your car get? "))
price_of_gas = float ( input("What is the price of gas per gallon? "))
number_of_travelers = int( input("How many people are travelling? "))

#CALCULATIONS
total_miles = trip_distance * 2
gallons_needed = total_miles / miles_per_gallon
gas_cost = gallons_needed * price_of_gas
cost_per_traveler = gas_cost / number_of_travelers

#PRINT
print(f"Trip Summary for {first_name}")
print(f"Destination: {trip_destination}")
print(f"Total Gas Cost: ${gas_cost:.2f}")
print(f"Cost Per Traveler: ${cost_per_traveler:.2f}")
print("Safe Travels!")

