class CAR:
    def __init__(self, model_name, color, price, top_speed):
        self.model_name = model_name
        self.color = color
        self.price = price
        self.top_speed = top_speed

    def display(self):
        print("Car Details:")
        print(f"Model Name: {self.model_name}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(f"Top Speed: {self.top_speed}")


def main():
    car = []
    n = int(input("enter the number of details ypu want do display"))
    # car1 = CAR("Toyota Camry", "Blue", 25000, 120)
    # car2 = CAR("Tesla Model S", "Black", 80000, 155)
    #
    # # Display details of car1
    # car1.display_details()
    #
    # # Display details of car2
    # car2.display_details()

    for i in range(0, n):
        model_name = input("enter the model_name\n")
        color = input("enter the color\n")
        price = int(input("enter the price\n"))
        top_spped = int(input("enter the top speed\n"))
        cars = CAR(model_name, color, price, top_spped)
        car.append(cars)

    print("details of car are\n")
    for cars in car:
        cars.display()


if __name__ == "__main__":
    main()

# without use of constructor
# class Car:
#     def set_details(self, model_name, color, price, top_speed):
#         self.model_name = model_name
#         self.color = color
#         self.price = price
#         self.top_speed = top_speed
#
#     def read_details(self):
#         print("Model Name:", self.model_name)
#         print("Color:", self.color)
#         print("Price:", self.price)
#         print("Top Speed:", self.top_speed)
#
# # Creating an instance of Car
# my_car = Car()
#
# # Setting details using the set_details method
# my_car.set_details("Tesla Model S", "Black", "$80,000", "155 mph")
#
# # Displaying details
# my_car.read_details()
