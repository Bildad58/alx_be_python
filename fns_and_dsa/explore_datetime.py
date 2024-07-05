from datetime import datetime , timedelta

def display_current_datetime():   
    current_date = datetime.now( )
    print(f"Current date and time: {current_date}")

display_current_datetime()

number_of_days = int(input("Enter number of days to add to current date:"))

def calculate_future_date(YYYY, MM, DD):
       current_date = datetime.datetime(2024, 7, 5, 12, 45, 23, )
 
       time_delta = datetime.timedelta(days= {number_of_days})
       future_date = current_date + time_delta()
       print(f"Future date: {future_date}")

calculate_future_date(2024, 7, 5)
