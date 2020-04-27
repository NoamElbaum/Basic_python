class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(self.a, self.b)

    def add(self):
        return(self.a + self.b)

    def sub(self):
        return(self.a - self.b)

cal1 = Calculator(5, 8)

print(cal1.add())
print(cal1.sub())