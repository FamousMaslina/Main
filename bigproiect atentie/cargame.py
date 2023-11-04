import random

class Car:
    def __init__(self, make, model, top_speed, acceleration):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.current_speed = 0

    def accelerate(self):
        self.current_speed += self.acceleration

    def decelerate(self):
        self.current_speed -= self.acceleration

    def brake(self):
        self.current_speed = 0

    def get_current_speed(self):
        return self.current_speed

    def get_info(self):
        return "Make: {}\nModel: {}\nTop speed: {}\nAcceleration: {}\n".format(self.make, self.model, self.top_speed, self.acceleration)

def generate_real_car(car_number):
    top_speeds = {
        1: 120, # Honda Accord
        2: 130, # Toyota Camry
        3: 140, # Ford F-150
        4: 150, # Chevrolet Silverado
        5: 160, # Nissan Altima
    }

    accelerations = {
        1: 0.5, # Honda Accord
        2: 0.6, # Toyota Camry
        3: 0.7, # Ford F-150
        4: 0.8, # Chevrolet Silverado
        5: 0.9, # Nissan Altima
    }

    top_speed = top_speeds[car_number]
    acceleration = accelerations[car_number]

    # Fixed: return Car object with correct arguments
    return Car(make="Toyota", model="Camry", top_speed=top_speed, acceleration=acceleration)

def race(car1_number, car2_number, cars):
    car1 = cars[car1_number]
    car2 = cars[car2_number]

    while car1.get_current_speed() < car1.top_speed and car2.get_current_speed() < car2.top_speed:
        car1.accelerate()
        car2.accelerate()

    if car1.get_current_speed() >= car1.top_speed:
        winner = car2
    else:
        winner = car1

    return winner

def main():
    # Create a list of cars
    cars = []
    for car_number in range(1, 6):
        car = generate_real_car(car_number)
        cars.append(car)

    # Print the list of cars and ask the user to choose two cars
    print("Choose a car for player 1:")
    for car_number, car in enumerate(cars):
        print(f"{car_number + 1}: {car.get_info()}")

    car1_number = int(input("Enter the number of the car you want: ")) - 1

    print("Choose a car for player 2:")
    for car_number, car in enumerate(cars):
        print(f"{car_number + 1}: {car.get_info()}")

    car2_number = int(input("Enter the number of the car you want: ")) - 1

    # Race the two cars and print the winner
    winner = race(car1_number, car2_number, cars)
    print(f"The winner is: {winner.model}")

if __name__ == "__main__":
    main()
    input()
