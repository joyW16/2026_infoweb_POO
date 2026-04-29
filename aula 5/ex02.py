class Triangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h/2
    def __str__(self):
        return f"Eu sou um triângulo, minha base é {self.__b} e minha altura é {self.__h}"
    

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
    @staticmethod
    def menu():
         print("1-Triangulo 9-Fim")
         op = int(input("Escolha uma opção:"))
         return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        b = float