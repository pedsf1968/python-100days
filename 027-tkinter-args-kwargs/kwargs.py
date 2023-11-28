def function_with_unlimited_arguments(*args):
    for n in args:
        print(n)


def add(*args):
    result = 0
    for number in args:
        result += float(number)
    return result


def function_with_unlimited_key_values(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {kwargs[key]}")


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car( object):

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model", "i30")
        self.color = kwargs.get("color", "white")

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Color: {self.color}")


def main():
    function_with_unlimited_arguments(1, 2, 3, "four", "five", ("six", 7))
    print(add(1, 23, 65, 7, 9, 7, 9, 879))

    function_with_unlimited_key_values(add=3, mult=5)
    calculate(5, add=3, multiply=5)

    my_car = Car(make="kia", model="ceed")
    my_car.display()


if __name__ == '__main__':
    main()
