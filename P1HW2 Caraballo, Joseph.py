# Caraballo, Joseph
# 20 June 2024
# P1HW2
# Creating a Budget calculator program for traveling

def travel_expenses(): 
    print("This program calculates and displays travel expenses")
    budget = float(input("Enter Budget: $"))
    destination = input("Enter your travel destination: ")
    gas_cost = float(input("How much do you think you will spend on gas: $")) 
    hotel_cost = float(input("Approximately, how much will you need for accomodation/hotel: $"))
    food_cost = float(input("Last, how much do you need for food: $"))

    total_expenses = gas_cost + hotel_cost + food_cost
    remaining_balance = budget - total_expenses

    print("\n------------Travel Expenses------------")
    print(f"Location: {destination}")
    print(f"Initial Budget: ${budget:.2f}")
    print(f"Fuel: ${gas_cost:.2f}")
    print(f"Accomodation: ${hotel_cost:.2f}")
    print(f"Food: ${food_cost:.2f}")
    print(f"Remaining Balance: ${remaining_balance:.2f}")
travel_expenses()