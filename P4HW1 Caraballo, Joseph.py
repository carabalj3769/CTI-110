# Caraballo, Joseph
# 9 July 2024
# P4Lab2
# Making a Multiplication Table

def collect_scores(num_scores): 
    """Collect a specified number of scores from the user, ensuring each score is valid.""" 
    scores = [] 
    for i in range(num_scores): # program pseudocode
        while True: 
            try: 
                score = float(input(f"Enter score {i + 1}: ")) 
                if 0 <= score <= 100: 
                     scores.append(score) 
                     break # Exit the inner loop if the score is valid 
                else: 
                    print("Invalid score. Score must be between 0 and 100.") 
            except ValueError: 
                print("Invalid input. Please enter a number between 0 and 100.") 
    return scores 

def calculate_average(scores): 
    """Calculate the average of scores.""" 
    if not scores: 
        return 0 
    return sum(scores) / len(scores) 

def calculate_grade(average_score): 
    """Calculate a simple grade based on average score.""" 
    if average_score >= 90: 
        return 'A' 
    elif average_score >= 80: 
        return 'B' 
    elif average_score >= 70: 
        return 'C' 
    elif average_score >= 60: 
        return 'D' 
    else: 
        return 'F' 
        
def display_results(scores):
    """Display the results including lowest score, modified list, average, and grade."""
    print("--------------------Results--------------------")

    lowest_score = min(scores) if scores else 0
    print(f"{'Lowest Score:':<20} {lowest_score:>5.2f}" )

    modified_scores = [score * 2 for score in scores]
    print(f"{'Modified scores:':<20} {', '.join(f'{s:.2f}' for s in modified_scores):>10}")

    average_score = calculate_average(scores)
    print(f"{'Average score:':<20} {average_score:>5.2f}")

    grade = calculate_grade(average_score)
    print(f"{'Grade:':<20} {grade:>1}")
    print("-----------------------------------------------")

def main():   
 while True:
     try:
        num_scores = int(input("Enter the number of scores you would like to enter: ")) 
        if num_scores > 0: 
           scores = collect_scores(num_scores) 
           display_results(scores)
        else:
           print("Please enter a positive integer")
     except ValueError: 
         print("Invalid input. Please enter a valid integer.") 
     while True: 
      repeat = input("Do you want to enter more scores? (yes/no): ").strip().lower() 
      if repeat == 'yes': 
          break # Exit the inner loop to ask for a new number of scores 
      elif repeat == 'no': 
          print("Goodbye!") 
          return # Exit the program 
      else: 
          print("Please enter 'yes' or 'no'.")

if __name__ == "__main__": main()
