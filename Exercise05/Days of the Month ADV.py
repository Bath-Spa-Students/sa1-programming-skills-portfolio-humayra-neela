def Days_of_the_Months(Month, Year):

    # Inserting Months as serial Numbers and Days of those months
    if Month in [1,   #January
                 3,   #March    
                 5,   #May
                 7,   #July
                 8,   #August
                 10,  #October
                 12]: #December
        return 31 #Seven months in a year are 31 days
    
    elif Month in [4,   #April
                   6,   #June
                   9,   #September
                   11]: #November
        return 30 #four months in a year are 30 days
    
    elif Month == 2:  #February

        # Checking if its a leap year or not
        if leap_year(Year):
            return 29 #in leap year February has 29 days
        else:
            return 28 #in normal years February remains with 28 days
    else:
        return "Invalid Number. Please Enter the correct Month number." #in case the user puts different number which is not between (1-12)

def leap_year(Year):
    # Acknowledging if it's a Leap year
    return (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0)

# Asking for user input
Month = int(input("Enter the month (1-12): "))
Year = int(input("Enter the year: "))

# Get and display the number of days in the specified month
Days = Days_of_the_Months(Month, Year)
print(f"The number of days in month {Month} of the year {Year} is: {Days}")