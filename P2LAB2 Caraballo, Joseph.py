# Caraballo, Joseph
# 21 June 2024
# P2LAb1
# Creating a Dictionary program for Cars and their MPG

def vehicles_mpg():
    vehicles = {
        "Camaro": 18.21,
        "Prius": 52.36,
        "Model S": 110,
        "Silverado": 26
    } 
    print("dict_keys(['Camaro', 'Prius', 'Model S', 'Silverado'])")
    
    vehicle = input("\nEnter a vehicle to see it's mpg: ")
    if vehicle in vehicles:
        mpg = vehicles[vehicle]
        print(f"The {vehicle} gets {mpg} mpg.")

        miles = float(input(f"How many miles will you drive the {vehicle}? "))
        
        gallons_needed = miles / mpg
        print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.2f} miles")
    else: print("Sorry, the vehicle you entered isn't part of the list")

vehicles_mpg()