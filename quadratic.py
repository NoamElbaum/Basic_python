import math


class QuadError(Exception):
    def __init__ (self, msg):
        super().__init__(msg)


def calculate_quadratic_equation(a, b, c):

        if (b*b - 4*a*c) < 0 or a == 0:
            raise QuadError("The equation is not quadratic")
        else:
            x1 = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
            x2 = ((-b) - math.sqrt(b*b - (4*a*c))) / (2*a)
            result = [x1, x2]
            return result


print(calculate_quadratic_equation(5, 7, -15))
print(calculate_quadratic_equation(6, 11, -35))
print(calculate_quadratic_equation(2, 4, -2))
print(calculate_quadratic_equation(2, 0, -64))
print(calculate_quadratic_equation(-12, 13, 0))
print(calculate_quadratic_equation(6, 11, -35))
print(calculate_quadratic_equation(0, 11, 50))
