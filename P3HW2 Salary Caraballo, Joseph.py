# Caraballo, Joseph I.
# 1 July 2024
# P3HW2
# Salary Calculator Breakdown Program

def main(): 
    name = input("Enter employee's name: ") 
    hours_worked = float(input("Enter number of hours worked: ")) 
    pay_rate = float(input("Enter employee's pay rate: "))
    
    overtime_rate = 1.5 
    standard_hours = 40 
    
    if hours_worked > standard_hours: 
       regular_hours = standard_hours 
       overtime_hours = hours_worked - standard_hours 
    else:
       regular_hours = hours_worked 
       overtime_hours = 0 
        
    regular_pay = regular_hours * pay_rate 
    overtime_pay = overtime_hours * pay_rate * overtime_rate 
    gross_pay = regular_pay + overtime_pay 
      
    print(f"\nEmployee name: {name}") 
    print() 
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("-" * 90) 
    print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}") 
        
if __name__ == "__main__": 
    main()