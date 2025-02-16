"""
Object Iteration: iter and next

Make custom objects iterable using loops
"""
from itertools import count


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


if __name__ == '__main__':


    # Create an instance of Countdown starting from 5
    countdown_from_5 = Countdown(5)

    # Iterate over the countdown using a for loop
    for number in countdown_from_5:
        print(number)


