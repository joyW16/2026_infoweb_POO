class Endereco:
    def __init__(self, id, nome, endereco, id_cliente):
        self.set_id(id)
        self.set_nome(nome)
        self.set_endereco(endereco)
        self.set_id_cliente(id_cliente)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_endereco(self, endereco):
        if endereco == "": raise ValueError("Endereço deve ser informado")
        self.__endereco = endereco
    def set_fone(self, id_cliente):
        if id_cliente < 0: raise ValueError("O id do cliente deve ser informado")
        self.__id_cliente = id_cliente
    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha deve ser informada")
        self.__senha = senha
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_endereco(self): return self.__endereco
    def get_id_cliente(self): return self.__id_cliente
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__endereco} - {self.__id_cliente}"
    def to_json(self):
        return { "id": self.__id, 
                "nome": self.__nome, 
                "endereço": self.__endereco, 
                "id_cliente": self.__id_cliente, }
    @staticmethod
    def from_json(dic):
        return Endereco( dic["id"], dic["nome"], dic["endereço"], dic["id_cliente"] )