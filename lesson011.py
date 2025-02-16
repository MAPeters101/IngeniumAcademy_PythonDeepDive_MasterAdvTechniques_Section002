"""
Callable Objects: call

Make an instance of a class callable like a function

"""

class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f'{self.greeting}, {name}!'

    def greet(self, name):
        return f'{self.greeting}, {name}!'


if __name__ == '__main__':
    hello = Greeter("Hello")

    print(hello('John'))
    print()
    print(hello.greet('John'))