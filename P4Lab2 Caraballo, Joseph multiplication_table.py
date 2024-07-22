# Caraballo, Joseph
# 9 July 2024
# P4Lab2
# Making a Multiplication Table

def display_multiplication_table(n):
     """Display the multiplication table for n from 1 to 12.""" 
     print(f"Multiplication table for {n}:") 
     for i in range(1, 13): 
         print(f"{n} x {i} = {n * i}") 
         
def main(): 
    while True: 
        try: 
            user_input = int(input("Enter an integer: ")) 
            if user_input < 0: print("Cannot accept negative values.") 
            else: display_multiplication_table(user_input)
        except ValueError: 
                print("Invalid input. Please enter a valid integer.")
                continue  # Prompt the user again for an integer
        while True: 
            repeat = input("Do you want to run it again? (yes/no): ").strip().lower() 
            if repeat == 'yes': 
                break # Exit the inner while loop to ask for a new integer
            elif repeat == 'no': 
                print("Goodbye!") 
                return # Exit the program
            else: print("Please enter 'yes' or 'no'.")
            
if __name__ == "__main__": main()
