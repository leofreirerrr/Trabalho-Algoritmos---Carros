carros = []
termo  = ""
op = 0

def cadastro():
    marca = str(input("Insira a marca do carro: "))
    modelo =str(input("insira modelo do carro: "))
    ano = int(input("Insira o ano-modelo do veículo: "))
    aut = float(input("Insira quantos km o veículo faz por litro: "))
    carros.append({
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "autonomia": aut
    })

def search():
    termo = str(input("Insira o termo de busca: "))
    for carro in carros:
        if termo.lower() == carro['marca'].lower() or termo.lower() == carro['modelo'].lower():
            print(f"Marca: {carro['marca']}   |   Modelo: {carro['modelo']}   |   Ano: {carro['ano']}   |   Autonomia: {carro['autonomia']} km/l")

bem_vindo = """BEM VINDO"""
menu = """O que deseja fazer agr?
[1] - Cadastrar um novo veículo 
[2] - Buscar por algum veículo existente
[3] - Mostrar carro específico ou todos os carros existentes
[4] - Sair
Insira a opção desejada: """


def main():
    print(bem_vindo)
    op = int(input(menu))
    while op!= 4 and op>=1:
        if op == 1:
            cadastro()
        elif op == 2:
            search()
        elif op == 3:
            print(bem_vindo)
        elif op == 4:
            print("Obrigado por utilizar o sistema")
        else:
            print("Opção inválida!")

        op = int(input(menu))


main()