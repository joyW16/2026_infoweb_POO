from datetime import datetime

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_data(self, data):
        if data > datetime.now(): raise ValueError("Data não pode ser no futuro")
        self.__data = data
    def set_distancia(self, distancia):
        if distancia <= 0: raise ValueError("Distância deve ser maior que zero")
        self.__distancia = distancia
    def set_tempo(self, tempo):
        if tempo <= 0: raise ValueError("Tempo deve ser maior que zero")
        self.__tempo = tempo
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def pace(self):
        return self.__tempo/self.__distancia
    def __str__(self):
        return f"{self.__id} - " + \
               f"{self.__data.strftime("%d/%m/%y")} - " + \
               f"{self.__distancia:.2f} km - " + \
               f"{self.__tempo:.2f} min - " + \
               F"Pace: {self.pace():.2f} min/km"
    
class TreinoUI: 
    __treinos = []
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.maisrapido()
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Listar por id 4-Atualizar 5-Excluir 6-O Treino mais rápido ")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        data = datetime.strptime(input("Informe a data (dd/mm/aaaa): "), "%d/%m/Y")
        distancia = float(input("Informe a distância em km: "))
        tempo = float(input("Informe o tempo em minutos: "))
        x = Treino(id, data, distancia, tempo)
        cls.__treinos.append(x)
    @classmethod
    def listar(cls):
        if len(cls.__treinos) == 0: 
            print("Nenhum treino cadastrado")
        else:
            for x in cls.__treinos:
                print(x)
    @classmethod
    def listar_id(cls):
        id = int(input("Informe o id do treino: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                print(x)
            else:
                print("Treino não encontrado")
    @classmethod
    def atualizar(cls):
        for x in cls.__treinos:
            print(x)
        id = int(input("Informe o id do trenio a ser atualizado: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                data = datetime.strftime(input("Informe a nova data (dd/mm/aaaa): "), "%d/%m/%y")
                distancia = float(input("Informe a nova distância: "))
                tempo = float(input("Informe o novo tempo: "))
                x.set_data(data)
                x.set_distancia(distancia)
                x.set_tempo(tempo)
                
    @classmethod
    def excluir(cls):
        for x in cls.__treinos:
            print(x)
        id = int(input("Informe o id do treino a ser excluido: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                cls.__treinos.remove(x)
    @classmethod
    def mais_rapido(cls):
        if len(cls.__treinos) == 0:
            print("Nenhum treíno cadastrado")
        melhor = cls.__treinos[0]
        for x in cls.__treinos:
            if x.pace() < melhor.pace():
                melhor = x
        print("Treino mais rápido: ")
    
TreinoUI.main()