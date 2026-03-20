mes = int(input("Digite o número do mês:"))
nomes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
if 1 <= mes <= 12:
    if mes <= 3:
        tri = "primeiro"
    elif mes<= 6:
        tri = "segundo"
    elif mes <= 9:
        tri = "terceiro"
    else:
        tri = "quarto"
    print(f"O mês de {nomes[mes]} é do {tri} trimestre do ano")
else: 
    print("Mês inválido")

