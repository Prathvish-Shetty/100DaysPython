def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
        # print(n)
    return sum


# print("sum = ", add(1, 2, 3))

# kwargs : many keyworded arguments

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car()
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)
# print(my_car)
