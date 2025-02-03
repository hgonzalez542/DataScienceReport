# Dictionary of names and birthdays
birthdays = {
    "Hector": "January 5, 1995",
    "Bob": "March 12, 1993",
    "Charles": "July 22, 1998",
    "Dave": "October 30, 1990"
}

# Ask the user for a name
name = input("Enter a name: ")

# Look up and print the birthday
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print("Sorry, I don't have that person's birthday.")