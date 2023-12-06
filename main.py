print("Welcome to the Rollercoaster!!!!")
height = int(input("What is your height in cm?"))

if height >=  120:
    print("You can ride the Rollercoaster.")
    age = int(input("What is your age \n"))
    if age < 12:
        print("Please pay $5.00 ")
    elif age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("You are too short to ride the rollercoaster.")