"""
Arithmetic Operations

Implement operations like addition, subtraction, and multiplication for custom
objects
"""

class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.imag = image

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.imag * other.real - self.real * other.imag
        return ComplexNumber(real_part, imag_part)








