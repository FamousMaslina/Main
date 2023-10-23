from api import *
import requests
class Country:
  def __init__(self, name, population, stability, oil):
    self.name = name
    self.population = population
    self.stability = stability
    self.oil = oil

  def add_oil(self, amount):
    self.oil += amount

  def get_oil(self):
    return self.oil

  def get_stability(self):
    return self.stability

  def get_population(self):
    return self.population

  def get_name(self):
    return self.name

alg = Country("Algeria", 45000000, random.randint(0, 100), 50000)
lib = Country("Libya", 6000000, random.randint(0, 100), 2000000)
eri = Country("Eritrea", 3600000, random.randint(0, 100), 3000)


def main():
  money = 250000
  countries = [alg, lib, eri]

  while True:
    clear()
    print(money, "cash")
    linebr(25)
    print("1 - Steal an oil field")
    print("2 - Skip Turn")
    print("3 - Country List")
    linebr(25)
    choice = input("> ")
    if choice == "1":
        while True:
            clear()
            print(money, "cash")
            print("Algeria has {} oil".format(alg.get_oil()))
            print("Libya has {} oil".format(lib.get_oil()))
            print("Eritrea has {} oil".format(eri.get_oil()))
            linebr(25)
            sol = 5000
            recr = int(input("Enter amount: "))




if __name__ == "__main__":
  main()