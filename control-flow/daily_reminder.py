task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Use match-case to process based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority level."

# Step 3: Adjust message if task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    if priority == "low":
        reminder += " Consider completing it when you have free time."
    elif priority == "medium":
        reminder += " Try to get it done soon, but it’s not urgent."

    # Step 4: Print customized reminder
print("\nReminder:", reminder)
