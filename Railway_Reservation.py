#Here's some sample Python code for a Railway Reservation System:

class Train:

    def __init__(self, name, source, destination, fare, seats):
        self.name = name
        self.source = source
        self.destination = destination
        self.fare = fare
        self.seats = seats

    def display_train(self):
        print("Train Name:", self.name)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Fare:", self.fare)
        print("Available Seats:", self.seats)


trains = []

def add_train():
    name = input("Enter Train Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    fare = int(input("Enter Fare: "))
    seats = int(input("Enter Seats: "))

    train = Train(name, source, destination, fare, seats)
    trains.append(train)
    print("Train Added Successfully!")


def display_trains():
    for train in trains:
        train.display_train()


def reserve_seat():
    name = input("Enter Train Name: ")
    for train in trains:
        if train.name == name:
            if train.seats > 0:
                train.seats -= 1
                print("Seat Reserved Successfully!")
                break
            else:
                print("Sorry, No Seats Available!")


while True:
    print("\n\n********** WELCOME TO RAILWAY RESERVATION **********")
    print("1. Add Train")
    print("2. Display Trains")
    print("3. Reserve Seat")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_train()

    elif choice == 2:
        display_trains()

    elif choice == 3:
        reserve_seat()

    elif choice == 4:
        print("Thank You For Using Our Service!")
        break

    else:
        print("Invalid Choice. Please Try Again.")

