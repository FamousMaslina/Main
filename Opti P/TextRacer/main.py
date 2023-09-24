import numpy as np
def calculate_drag_race_winner(car1, car2):
  """Calculates the winner of a drag race between two cars.

  Args:
    car1: A dictionary containing the specifications of the first car.
    car2: A dictionary containing the specifications of the second car.

  Returns:
    The name of the car that won the drag race.
  """

  # Calculate the power-to-weight ratio of each car.
  car1_power_to_weight_ratio = car1["horsepower"] / car1["weight"]
  car2_power_to_weight_ratio = car2["horsepower"] / car2["weight"]

  # Calculate the acceleration of each car.
  car1_acceleration = car1_power_to_weight_ratio * 9.8
  car2_acceleration = car2_power_to_weight_ratio * 9.8

  # Calculate the time it takes each car to reach 60 mph.
  car1_time_to_60 = car1_acceleration * car1["0-60 time"]
  car2_time_to_60 = car2_acceleration * car2["0-60 time"]

  # Calculate the top speed of each car.
  car1_top_speed = car1["top speed"] * 0.621371
  car2_top_speed = car2["top speed"] * 0.621371

  # Calculate the reaction time of each car.
  car1_reaction_time = np.random.rand() * 0.5
  car2_reaction_time = np.random.rand() * 0.5

  # Calculate the traction of each car.
  car1_traction = np.random.rand() * 0.9
  car2_traction = np.random.rand() * 0.9

  # Calculate the aerodynamics of each car.
  car1_aerodynamics = np.random.rand() * 1.1
  car2_aerodynamics = np.random.rand() * 1.1

  # Calculate the time it takes each car to reach the finish line.
  car1_time_to_finish = car1_time_to_60 + (car1_top_speed / (car1_acceleration * car1_traction * car1_aerodynamics)) * 402
  car2_time_to_finish = car2_time_to_60 + (car2_top_speed / (car2_acceleration * car2_traction * car2_aerodynamics)) * 402

  # If the two cars have the same time to the finish line, the winner is the car with the higher top speed.
  if car1_time_to_finish == car2_time_to_finish:
    if car1_top_speed > car2_top_speed:
      return car1["name"]
    else:
      return car2["name"]

  # Otherwise, the winner is the car with the shorter time to the finish line.
  else:
    if car1_time_to_finish < car2_time_to_finish:
      return car1["name"]
    else:
      return car2["name"]


if __name__ == "__main__":
  # Create two cars with different specifications.
  car1 = {
      "name": "Peugeot 205 GTi",
      "horsepower": 128,
      "torque": 161,
      "weight": 860,
      "0-60 time": 7.8,
      "top speed": 128,
      "gears": 5
  }

  car2 = {
      "name": "Mazda RX-7 FD",
      "horsepower": 255,
      "torque": 294,
      "weight": 300,
      "0-60 time": 5.3,
      "top speed": 155,
      "gears": 5
  }

  # Calculate the winner of the drag race.
  winner = calculate_drag_race_winner(car1, car2)

  # Print the winner of the drag race.
  print(f"The winner of the drag race is {winner}!")
