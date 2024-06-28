#prompt the user the input the following
task = input("Enter your task:") 
priority = input("Priority (high/medium/low):")
time_bound =input("Is it time-bound? (yes/no):")

#use match case to react to the inputs
match priority:
     case 'high':
          if time_bound == 'yes':
           print("{task}, is a  high priority task that requires immediate attention today!")
          else:
              print(f"{task}, is a high priority task that requires immediate attention today!") 
          
     case 'medium':
        if time_bound == 'yes':
            print("{task},  is a high priority task that requires immediate attention today!")
        else:
            print(f"{task}, is a high priority task that requires immediate attention today!")

     case 'low':
        if time_bound == 'yes':   
            print(f"{task}, is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"{task} , is a low priority task. Consider completing it when you have free time.'")    

