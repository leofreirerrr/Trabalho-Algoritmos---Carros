carros = []
termo  = ""
op = 0
aut = []

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
    while op!= 4:
        if op == 1:
            cadastro()
        elif op == 2:
            termo = str(input("Insira o termo para busca: "))
            for carro in carros:
               print("oi")
         
        elif op == 3:
            for i in range(len(carros)):
                print(f"marca : {carros[i]["marca"]}  |  Modelo : {carros[i]["modelo"]}  | Ano : {carros[i]["ano"]} , autonomia : {carros[i]["autonomia"]}")
        else:
            print("Opção inválida!")

        op = int(input(menu))


main()