 # Caraballo, Joseph
 # 20 June 2024
 # P1HW1
 # A Calculator


def exponentiate(base, exponent): return base ** exponent

def main_exponents():
    print("-----Calculating Exponents-----")
    base = float(input("Enter an integer as the base value: "))
    exponent = float(input("Enter an integer as the exponent: "))
    result = exponentiate(base, exponent)
    print(f"{base} raised to the power of {exponent} is equal to {result}")

    

def calculate(starting_integer, integer_to_add, integer_to_subtract):
    result = starting_integer + integer_to_add - integer_to_subtract 
    return result

def main_add_and_sub():
    print("-----Addition & Subtraction-----")

    starting_integer = int(input("Enter a starting integer: "))
    integer_to_add = int(input("Enter a integer to add: "))
    integer_to_subtrac = int(input("Enter a integer to subtract: "))

    result = calculate("starting_integer; integer_to_add; integer_to_subtract")

    print(f"Enter Starting Integer: {starting_integer}")
    print(f"Enter Integer To Add: {integer_to_add}")
    print(f"Enter Integer To Subtract: {integer_to_subtrac}")
    print(f"{starting_integer} + {integer_to_add} - {integer_to_subtrac} is equal to {result}")

if __name__ == "__main__": 
    min()
