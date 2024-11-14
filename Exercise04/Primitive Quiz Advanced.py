# It's A Python Dictionary storing countries and their capitals for the Quiz which the user will answer to get Score.

# Inputing country names and their capitals
Country_Capital = {
    "France": "Paris",
    "Denmark": "Copenhagen",
    "Switzerland": "Bern",
    "Finland": "Helsinki",
    "Poland": "Warsaw",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Slovenia": "Ljubljana",
    "Serbia": "Belgrade",
    "Ukraine": "Kyiv"
}

score = 0  #To keep track of the user's score

# Looping through each country-capital pair in the Quiz
for country, capital in Country_Capital.items():
    # Ask the user for the capital of the current country
    Result = input(f"What's the capital of {country}? ")

    # Using 'if-else' conditions to acknowledge the answer with case insensitive words.
    if Result.lower() == capital.lower():
        # If correct adding 1 point to the score
        print("That's a correct Answer.")
        score += 1
    else:
        # if Wrong, Adding the correct answer for User's Knowledge.
        print(f"Oops the capital of {country} is actually {capital}. Better Luck for the Next one")

# Displaying the User's final score.
print(f"\nYAY!Congratulations You scored {score} out of {len(Country_Capital)}.")