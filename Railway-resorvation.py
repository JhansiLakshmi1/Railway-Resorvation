class Train:
    def __init__(self,name,Trainnum,fare,seats):
        self.name = name
        self.Trainnum = Trainnum
        self.fare = fare
        self.name = name
        self.seats = seats
    
    def getInfo(self):
        print("________________________________________________________")
        print(f"The name of Train is{self.name} and Train Number is {self.Trainnum}")
        print(f"The fare for the journey is Rs: {self.fare}")
        print(f"The number of avilable seats in the train are {self.seats}")
        print("_________________________________________________________")
    def bookTicket(self):
        if self.seats > 0:
            print(f"Congratulations your ticket has been booked and your seat number is {self.seats}")
        else:
            print("Sorry, there are no seats available in the train. please try Tatkal")
        self.seats = self.seats -1

t = Train("Rajdhani", 22012, 1439 ,2)
t.getInfo()        
t.bookTicket()
t.bookTicket()
t.bookTicket()