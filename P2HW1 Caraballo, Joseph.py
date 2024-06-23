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

    label_width = 20
    value_width = 14

    print("\n------------Travel Expenses------------")
    print(f"{'Location:':<{label_width}}{destination:>{value_width}}")
    print(f"{'Initial Budget:':<{label_width}} ${budget:>{value_width - 8}.2f}")
    print(f"{'Fuel:':<{label_width}} ${gas_cost:>{value_width - 8}.2f}")
    print(f"{'Accomodation:':<{label_width}} ${hotel_cost:>{value_width - 8}.2f}")
    print(f"{'Food:':<{label_width}} ${food_cost:>{value_width - 8}.2f}")
    print("----------------------------------------")
    print()
    print(f"{'Remaining Balance:':<{label_width}} ${remaining_balance:>{value_width - 8}.2f}")
travel_expenses()