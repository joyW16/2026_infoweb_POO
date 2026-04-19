import math

class Triangulo:
    def __init__(self):
        self.__b = 0.0 #encapsulamento
        self.__h = 0.0
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
        return self.__b * self.__h / 2 
    
    
class Circulo:
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, v):
        if v >= 0: self.__raio = v
        else: raise ValueError()

    def get_raio(self):
        return self.__raio
    
    def calc_area(self):
        return math.pi * (self.__raio ** 2)
    
    def calc_circuferencia(self):
        return 2 * math.pi * self.__raio
    
    
class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__horas = 0
        self.__minutos = 0
    
    def set_distancia(self, v):
        if v >= 0: self.__distancia = v
        else: raise ValueError()

    def set_tempo(self, h, m):
        if h >= 0 and m >=0:
            self.__horas = h
            self.__minutos = m
        else:
            raise ValueError()
    
    def get_distancia(self):
        return self.__distancia
    
    def get_tempo(self):
        return (self.__horas, self.__minutos)
    
    def calc_velocidade(self):
        tempo_total = self.__horas + (self.__minutos / 60)
        return self.__distancia / tempo_total
    
class ContaBancaria:
    def __init__(self):
        self.__titular = ""
        self.__numero = 0
        self.__saldo = 0.0
    
    def set_titular(self, v):
        self.__titular = v

    def set_numero(self, v):
        self.__numero = v

    def set_saldo(self, v):
        if v >= 0: self.__saldo = v
        else: raise ValueError()
    
    def get_titular(self):
        return self.__titular
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, v):
        if v > 0: self.__saldo += v

    def sacar(self, v):
        if v <= self.__saldo:
            self.__saldo -= v
        else:
            print("Saldo insuficiente")


class EntradaCinema:
    def __init__(self):
        self.__dia = ""
        self.__hora = 0

    def set_dia(self, v):
        self.__dia = v.lower()

    def set_hora(self, v):
        if 0 <= v <= 23: self.__hora = v
        else: raise ValueError()

    def get_dia(self):
        return self.__dia
    
    def get_hora(self):
        return self.__hora
    
    def calc_valor(self):
        if self.__dia == "quarta":
            return 8
        
        if self.__dia in ["segunda", "terça", "quinta"]:
            valor = 16
        else:
            valor = 20
        if 17 <= self.__hora <= 23:
            valor *= 1.5

        return valor
    def calc_meia(self):
        return self.calc_valor() / 2
    
#interfarce do usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta()
            if op == 5: UI.ingresso()
    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária, 5-Ingresso, 9-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")
    @staticmethod
    def circulo():
        print("Calculo da área de um circulo")
        x = Circulo()
        
        print("")
    @staticmethod
    def viagem():
        print(float(input("Informe")))
    @staticmethod
    def conta():
        pass
    @staticmethod
    def ingresso():
      pass
    
UI.main()

