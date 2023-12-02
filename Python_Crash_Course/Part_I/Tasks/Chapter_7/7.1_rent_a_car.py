# Ex. 7.1 Rent a car
# Create a program that asks the user what brand of car he would like to rent. Then display a message along with the
# name of the car, for example: "Just a moment, let me see if we have a Subaru car available.".

car = input("Tell me what brand of vehicle you want to rent: ")

if car == "bmw":
    print(f"Just a moment, let me see if we have a {car.upper()} car available.")
else:
    print(f"Just a moment, let me see if we have a {car.title()} car available.")
