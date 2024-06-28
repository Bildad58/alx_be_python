#prompt the user the input the following
def main():
  
  task = input("Enter your task:")
  priority = input("Priority (high/medium/low):")
  time_bound =input("Is it time-bound? (yes/no:")

#use match case to react to the inputs
  match priority:
    case 'high':
        if 'yes':
         print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
    
    case 'low':
        if 'no':
           print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
           

