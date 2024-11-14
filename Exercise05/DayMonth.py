# Storing how many days in each month with Python Dictionary

#Using Numbers for each months.
Days_in_each_month = {
    1: 31,   # January
    2: 28,   # February
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10:31,  # October
    11:30,  # November
    12:31   # December
}

# Asking for Inputing the Number and using '.strip()' condition to remove extra spaces around input.
Month = int(input("Please enter a month number (1-12): ").strip())

# Using 'if-else' condition for the Answer.
if Month in Days_in_each_month:
        print(f"The number of days in this month {Month} is {Days_in_each_month[Month]}.")

else:
        print("That's not a valid Month number.")