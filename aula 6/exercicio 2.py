class País:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)


    def get_nome(self):
        return self.__nome
    
    def get_populacao(self):
        return self.__populacao
    
    def get_area(self):
        return self.__area
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome inválido.")
        self.__nome = nome

    def set_populacao(self, populacao):
        if populacao <= 0:
            raise ValueError("População deve ser maior que zero.")
        self.__populacao = populacao 

    def set_area(self, area):
        if area <= 0:
            raise ValueError("Área deve ser maior que zero.")
        self.__area = area

    def densidade(self):
        return self.__populacao / self.__area
    
class PaísUI:
    @staticmethod
    def menu():
        print("1-Calcular 2-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 2:
            if op == 1: PaísUI.Calculo()
    @staticmethod
    def Calculo():
        nome = input("Informe o nome do país: ")
        populacao = int(input("Informe a sua população: "))
        area = float(input("Informe a sua área em km2: "))
        x = País(nome, populacao, area)
        print(x.ToString())
        print(f"Densidade demográfica: {x.densidade():.2f} hab/km2")
        
PaísUI.main()