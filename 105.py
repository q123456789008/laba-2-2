first_letter = input("Enter the first letter: ")
second_letter = input("Enter the second letter: ")

if first_letter.lower() < second_letter.lower():
    print(f"{first_letter} is less than {second_letter}")
else:
    print(f"{first_letter} is not less than {second_letter}")
