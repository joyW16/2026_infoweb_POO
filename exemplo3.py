class Triangulo:
    def __init__(self):
        self.b = 0
    def calc_area(self):
     return self.b * self.h / 2
    
x = Triangulo()
x.b = 10
x.h = 20
y = x
y.b = 30
y.h = 40
print(x.b, x.h)

a = [1, 2, 3]
b = a
b.append(4)
print(a)
b = [1, 2, 3, 4, 5]
c = list()

print(type(x))
print(type(y))
print(type(a))
print(type(b))
print(type(c))

