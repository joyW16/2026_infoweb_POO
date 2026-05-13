class Time:
    def __init__(self,id, nome, estado):
        self.__id = id
        self.__nome = nome
        self.__estado = estado

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_estado(self):
        return self.__estado
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_estado(self, estado):
        self._estado = estado

    def __str__(self):
        return f"id: {self.__id}, Nome: {self.__nome}, Estado: {self.__estado}"
    
class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.__id = id
        self.__nome = nome
        self.__camisa = camisa
        self.__time = id_time

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_camisa(self):
        return self.__camisa
    
    def get_time(self):
        return self.__time
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_camisa(self, camisa):
        self.__camisa = camisa

    def set_id_time(self, time):
        self.__id_time = time

    def __str__(self):
        return f"id: {self.__id}, Nome: {self.__nome}, camisa: {self.__camisa}, id_time: {self.__time}"
    
class UI:
    time = []
    jogadores = []

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
            if op == 5: UI.inserir_jogador()
            if op == 6: UI.listar_jogadores()
            if op == 7: UI.atualizar_jogador()
            if op == 8: UI.excluir_jogador()
            if op == 9: UI.listar_jogadores_time()
            if op == 10: UI.transferir_jogador()

    @staticmethod
    def menu():
        print("1-Inserir time 2-Listar times 3-Atualizar time 4-Excluir time 5-Inserir jogador 6-Listar jogadores 7-Atualizar jogador 8-Excluir jogador 9-Listar jogadores do time 10=Transferir jogador 11-Sair")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def inserir_time():
        id = int(input("ID: "))
        nome = input("Nome: ")
        estado = input("Estado: ")
        UI.times.append(Time(id, nome, estado ))

    @staticmethod
    def listar_times():
        for t in UI.times:
            print(t)

    @staticmethod
    def atualizar_time():
        id = int(input("ID do time: "))
        for t in UI.times:
            if t.get_id() == id:
                UI.times.remove(t)

    @staticmethod
    def inserir_jogador():
        id = int(input("ID: "))
        nome = input("Nome: ")
        numero = int(input("Número: "))
        id_time = int(input("ID do time: "))
        UI.jogadores.append(Jogador(id, nome, numero, id_time))

    @staticmethod
    def listar_jogadores():
        for j in UI.jogadores:
            print(j)

    @staticmethod
    def atualizar_jogador():
        id = int(input("ID do jogador: "))
        for j in UI.jogadores:
            if j.get_id() == id:
                nome = input("Nome do novo jogador: ")
                numero = int(input("Número do novo jogador: "))
                j.set_nome(nome)
                j.set_numero(numero)

    @staticmethod
    def excluir_jogador():
        id = int(input("ID do jogador: "))
        for j in UI.jogadores:
            if j.get_id() == id:
                UI.jogadores.remove(j)

    @staticmethod
    def listar_jogadores_time():
        id_time = int(input("ID do Time: "))
        for j in UI.jogadores:
            if j.get_id_time() == id_time:
                print(j)
                
    @staticmethod
    def transferir_jogador():
        id = int(input("ID do jogador: "))
        novo_time = int(input("Novo ID do time: "))
        for j in UI.jogadores:
            if j.get_id() == id:
                j.set_id_time(novo_time)

UI.main()