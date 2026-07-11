from datetime import datetime, timedelta
class Avaliacao:
    def __init__(self, id, disciplina, local, data_hora):
        self.set_id(id)
        self.set_disciplina(disciplina)
        self.set_local(local)
        self.set_data_hora(data_hora)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_disciplina(self, disciplina):
        if disciplina == "": raise ValueError("Informe uma disciplina válida")
        self.__disciplina = disciplina
    def set_local(self, local):
        if local == "": raise ValueError("Informe um local válido")
        self.__local = local
    def set_data_hora(self, data_hora):
        if data_hora < datetime.now(): raise ValueError("Data deve ser no futuro")
        self.__data_hora = data_hora
    def get_id(self):
        return self.__id
    def get_disciplina(self):
        return self.__disciplina
    def get_local(self):
        return self.__local
    def get_data_hora(self):
        return self.__data_hora
    def __str__(self):
        return f"Id: {self.__id} - " + \
               f"Disciplina: {self.__disciplina} - " + \
               f"Local: {self.__local} - " + \
               f"Data: {self.__data_hora.strftime('%d/%m/%y %H:%M')}"
    
class AvaliacaoUI:
    objetos = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = AvaliacaoUI.menu()
            if op == 1: AvaliacaoUI.inserir()
            if op == 2: AvaliacaoUI.listar()
            if op == 3: AvaliacaoUI.proximos_dias()
    @staticmethod
    def munu():
        print("1-Inserir, 2-LIstar, 3-Próximos dias, 9-Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        discilina = input("Informe a disciplina: ")
        local = input("Informe o local: ")
        data_hora = datetime.strptime(input("Informe a data e hora: "), "%d/%m/%y %H:%M")
        x = Avaliacao(id, discilina, local, data_hora)
        cls.objetos.append(x)