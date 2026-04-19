class Triangulo:
    # atributo - dados que vão ser armazenados: b - base, h - altura
    def __init__(self):
        self.b = 0
        self.h= 0
    # método cálculo que vão ser feitos
    def calc_area(self):
        return self.b * self.h / 2

# x é a referência do objeto criado pela instrução Triangulo()
# x é um link <a href>
# Triangulo é pâgina
x = Triangulo()
print("Informe a base do triângulo")
x.b = float(input())
print("Informe o valor da altura")
x.h = float(input())
a = x.calc_area()
print(f"A área do primeiro triângulo é", x.calc_area())

y = Triangulo()
print("Informe a base do triângulo")
y.b = float(input())
print("Informe o valor da altura")
y.h = float(input())
b= y.calc_area()
print(f"A área do segundo triângulo é", y.calc_area())

print(f"Primeiro triângulo: base = {x.b}, altura = {x.h}, área = {x.calc_area()}")
print(f"Segundo triângulo: base = {y.b}, altura = {y.h}, área = {y.calc_area()}")