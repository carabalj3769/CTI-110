# Caraballo, Joseph
# 22 June 2024
# P2HW2
# Create a Module Grading program

def calculate_grades(grades):
    if not grades:
        return "No grades provided"
    
    lowest_grade = min(grades)
    highest_grade = max(grades)
    sum_of_grades = sum(grades)
    average_grade = sum_of_grades / len(grades)

    return {
        "Lowest Grade": lowest_grade,
        "Highest Grade": highest_grade,
        "Sum of Grades": sum_of_grades,
        "Average Grade": average_grade
    }
grades = []
for i in range(1, 7):
    while True:
        try:
            grade = float(input(f"Enter grade for Module {i}: "))
            grades.append(grade)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical grade.")

result = calculate_grades(grades)

if isinstance(result, dict):
    print("\n----------Results----------")
    print(f"{'Lowest Grade:':<15} {result['Lowest Grade']:>9}")
    print(f"{'Highest Grade:':<15} {result['Highest Grade']:>9}")
    print(f"{'Sum of Grades:':<15} {result['Sum of Grades']:>10}")
    print(f"{'Average:':<15} {result['Average Grade']:>10.2f}")
    print("____________________________")
else:
    print(result)