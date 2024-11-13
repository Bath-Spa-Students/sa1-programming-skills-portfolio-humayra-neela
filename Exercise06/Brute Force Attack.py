correct_password = "12345"

# 2. Use a while loop to repeatedly ask the user for the password until the correct one is entered
while input:
    user_input = input("Enter the password: ")

    # Check if the entered password is correct
    if user_input == correct_password:
        # Print it out
        print("Correct password!")
        break  # Exit the loop if the correct password is entered
    else:
        print("Incorrect password. Please try again.")