 # Caraballo, Joseph
 # 12 July 2024
  # P4HW2
  # A program that calculates gross pay for multiple employees and total amounts


def main(): 
    employees = [] 
    total_overtime_pay = 0 
    total_regular_pay = 0 
    total_gross_pay = 0 
    
    while True: 
        name = input("Enter employee's name or 'Done' to terminate: ") 
        if name.lower() == 'done': 
            break 
        hours_worked = float(input(f"How many hours did {name} work? ")) 
        pay_rate = float(input(f"What is {name}'s pay rate? ")) 
        
        overtime_hours = max(0, hours_worked - 40) 
        regular_hours = min(40, hours_worked) 
        overtime_pay = overtime_hours * (pay_rate * 1.5) 
        regular_pay = regular_hours * pay_rate 
        gross_pay = regular_pay + overtime_pay 
        
        employees.append((name, hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay)) 
        total_overtime_pay += overtime_pay 
        total_regular_pay += regular_pay 
        total_gross_pay += gross_pay 
        
        print(f"\nEmployee name: {name}") 
        print(f"Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay") 
        
        print("-------------------------------------------------------------------------------------") 
        
        print(f"{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12}{overtime_pay:<17.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")
        
    print("\nTotal number of employees entered:", len(employees)) 
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}") 
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}") 
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}") 
    
if __name__ == "__main__": 
    main()