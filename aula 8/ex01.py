class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    def to_json(self):
        return {"id" : self.id, "nome" : self.nome}
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"])
    
a = Cliente(1, "Douglas Crockford")
b = Cliente(2, "Jon Bosak")

a = Cliente(1, "Douglas Crockford") # chamado o __init__
b = Cliente(2, "Jon Bosak")
c = Cliente.from_json({ "id" : 3, "nome" : "Alan Turing"}) # chamado o from_json

print(a)
print(b)
print(c)
print(a.__dict__)
print(b.__dict__)
print(vars(a))
print(vars(b))
print(a.to_json())
print(b.to_json())