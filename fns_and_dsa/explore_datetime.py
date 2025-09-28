from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculates a future date by adding the specified number of days
    to the current date.
    """
    future_date = current_date + timedelta(days=days_to_add)

    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date
if __name__ == "__main__":
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt user and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer.")
# Part 2: Prompt user and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer.")