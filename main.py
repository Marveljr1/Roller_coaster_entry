print("Welcome to the Rollercoaster!!!!")
height = int(input("What is your height in cm?"))
bill = 0

if height >=  120:
    print("You can ride the Rollercoaster.")
    age = int(input("What is your age \n"))
    if age < 12:
        bill = 5
        print("Children tickets are $5.00 ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.00")
    else:
        bill = 12
        print("Adult tickets are $12.00")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You are too short to ride the rollercoaster.")