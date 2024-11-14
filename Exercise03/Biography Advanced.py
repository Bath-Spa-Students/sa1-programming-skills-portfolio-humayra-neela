# Inputing User Information questions.
name = input("Enter your full Name: ").strip()

hometown = input("Enter your Hometown: ").strip()

age = input("Enter your Age:").strip()
# Using input() so that the user can give their information
# .strip() Removes extra spaces in the input

# Print the collected informations
print("\nUser Information:")
print(f"Name: {name}")
print(f"Hometown: {hometown}")
print(f"Age: {age}")
