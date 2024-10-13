carros = []
def cadastro():#função de cadastro, na main tava com erro pra gerar outros dicionario 
    marca = str(input("Insira a marca do carro: ")).upper()
    modelo =str(input("insira modelo do carro: ")).upper()
    ano = int(input("Insira o ano-modelo do veículo: "))
    aut = float(input("Insira quantos km o veículo faz por litro na cidade: "))
    carros.append({
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "autonomia": aut
    })

def search():
    global termo
    termo = input("Digite por qual veículo você procura: ").upper()
    for carro in range(len(carros)):
        if termo == carros[carro]["marca"] or termo == carros[carro]["modelo"] or termo == str(carros[carro]["ano"]) or termo == str(carros[carro]["autonomia"]):
            print("Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l") #eu queria colocar num print(f) mas por algum caralho de motivo da erro qnd eu faço isso

def 

bem_vindo = """BEM VINDO"""
menu = """O que deseja fazer agr?
[1] - Cadastrar um novo veículo 
[2] - Buscar por algum veículo existente
[3] - Mostrar carro específico ou todos os carros existentes
[4] - Sair
Insira a opção desejada: """

op = 0
def main():
    print(bem_vindo)
    op = int(input(menu))
    while op!= 4:
        if op == 1:
            cadastro()
        elif op == 2:
            search()
        elif op == 3:
            print(bem_vindo)
        else:
            print("Opção inválida!")
        op = int(input(menu))
    print("Obrigado por utilizar o sistema!")
main()