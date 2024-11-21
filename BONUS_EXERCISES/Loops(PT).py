# Creating a programme with while loop where user can input pizza toppings

# printing a value to prompt the user to give information
print("Please enter the toppings you want and type 'quit' when you are done") 

while True :
    Pizza_Toppings = input("Topping you want: ")

    if  Pizza_Toppings.lower() == 'quit':  #using .lower() to make the input case insensitive
        print("Done with your pizza toppings.Hope you will enjoy it")
        break
    else :
        print (f"I'll add {Pizza_Toppings} to your pizza")