print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age <= 12:
        bill = 6
        print("Child Ticket are $6")
    elif age <= 18:
        bill = 8
        print("Youth Ticket are $8")
    else:
        bill = 12
        print("Adult ticket are $12")
    want_photo = input("Do you want to have your photo taken? Type y for Yes and n for No. ")
    if want_photo == "y":
        bill += 3
    print(f"Your final bill ${bill}")


else:
    print("Sorry you have to grow taller before you can ride")