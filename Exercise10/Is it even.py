# Creating a programme which identifies even or odd value with the main function

def even_or_odd(value):
    if value % 2 == 0:  # Even numbers can be divided by 2
        return f"The number {value} which you inputed is Even."
    else:  # Odd numbers divided by 2 creates a Float value 
        return f"The number {value} which you inputed is Odd." 

# Going through the Main function
def main():
    try:
        # Asking the user for value
        Input = int(input("Please enter any number: "))
        
        # Creating a variable for output
        result = even_or_odd(Input)

        print(result)

    except ValueError:   #If the user try to use anything eles than an integer value there will be a error
        print("Provided input is invalid. Try using ONLY INTEGER VALUE") 

# Run it in the main function as instructed
if __name__ == "__main__":
    main()