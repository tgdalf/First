print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 10:
        print("Your ticket will be $5")
    elif age <= 18:
        print("Your ticket will be $8")
    else:
        print("Your ticket will be $10")
else:
    print("Sorry, you are unable to ride the rollercoaster")