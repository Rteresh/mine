class Test:
    def __init__(self):
        self.num1 = 10
        self.num2 = 20

        self.num3 = self.num2 - self.num1

        self.y = False


test = Test()

for i in range(10):
    print(test.num3)

    test.num1 -= 1
    print(test.num1)

z = 5

def ss(num, test):
    num += 1
    test.y = True
    print(num, test.y)



ss(test.num2, test)
print(test.y)
