from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 17:
            op = UI.menu()
            #Clientes
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.cliente_pesquisar_nome()
            #Serviços
            if op == 6: UI.servico_inserir()
            if op == 7: UI.servico_listar()
            if op == 8: UI.servico_atualizar()
            if op == 9: UI.servico_excluir()
            if op == 10: UI.servico_pesquisar_descricao()
            #Profissionais
            if op == 11: UI.profissinal_inserir()
            if op == 12: UI.profissional_listar()
            if op == 13: UI.profissional_atualizar()
            if op == 14: UI.profissional_excluir()
            if op == 15: UI.profissional_pesquisar_id()
            if op == 16: UI.profissional_pesquisar_nome()

    @staticmethod
    def menu():
        print("-"*70)
        print(" [CLIENTES]     1-Inserir  2-Listar  3-Atualizar  4-Excluir  5-Pesquisar por Nome")
        print(" [SERVIÇOS]     6-Inserir  7-Listar  8-Atualizar  9-Excluir  10-Pesquisar por Descrição")
        print(" [PROFISSIONAL] 11-Inserir 12-Listar 13-Atualizar 14-Excluir 15-Buscar por ID 16-Buscar por Nome")
        print(" [SISTEMA]      17=Fim")
        print("-"*70)
        return int(input("Informe uma opção: "))
    
    #Clientes
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar():
            print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input("Informe o ID do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def cliente_pesquisar_nome():
        iniciais = input("Informe as iniciais do nome para pesquisar: ")
        encontrados = Service.cliente_listar_nome(iniciais)
        if len(encontrados) == 0:
            print("Nenhum cliente foi encontrado com essas iniciais")
        else:
            print("\n--- Clientes encontrados ---")
            for obj in encontrados:
                print(obj)
            
    #Serviços
    @staticmethod
    def servico_inserir():
        desc = input("Informe a descrição do serviço: ")