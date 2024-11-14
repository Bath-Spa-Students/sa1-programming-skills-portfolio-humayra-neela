# Entering the Specific Names
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Asking for Users input
Search_Name = input("Enter the name you want to search for: ")

# Using 'if-eles' condition for the Result
if Search_Name.lower() in [Name.lower() for Name in Names]: # Used ' .lower() ' condition to make this code case insensitive for the user
    print(f"'{Search_Name}' is in the list given.")
else:
    print(f"'{Search_Name}' isn't in the list given.")