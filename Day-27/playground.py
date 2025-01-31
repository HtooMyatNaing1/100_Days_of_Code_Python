def add(*args):
    sum_total = 0
    for i in args:
        sum_total += i
    return sum_total

print(add(1,2,3,4,5))

class Car:
    def __init__(self, **kwargs):
        self.maker = kwargs.get("maker")
        self.model =kwargs.get("model") # .get() method returns none if the value were not passed
        self.color = kwargs.get("color")

my_car = Car(maker="BMW", model="2025")
print(my_car.maker)
print(my_car.model)
print(my_car.color)