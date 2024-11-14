# Programming a code with limited Attempts to enter a password for access

# Informing about the correct password
password = "12345"

# Setting User Attempts
maximum_attempts = 5

attempts = 0 #Using a counter to track how many attempts made by the user

# Using 'while loop' that will run until the correct password is entered or the give max attempts are reached
while attempts < maximum_attempts:
    enter_password = input("Please enter the password: ").strip() # Just to avoid extra space in the Answer
    
    attempts += 1  # if incorrect, increment the attempts counter by 1

    # Checking if the input is the correct password
    if enter_password == password:
        print("Correct Attempt. Your Access has been Granted")
        break #If the input is correct stopping the loop there

    else:
        # for incorrect input counting the remaining attempts to inform the user
        remaining_attempts = maximum_attempts - attempts
        print(f"Sorry, the Password is Incorrect. You have {remaining_attempts} attempt(s) remaining.")
        
        if attempts == maximum_attempts:
            print("You have reached Maximum attempts. Authorities have been alerted about this.")