carros = []

#parte estética
bem_vindo = """BEM VINDO"""

menu = """O que deseja fazer agr?
[1] - Cadastrar um novo veículo 
[2] - Buscar por algum veículo existente
[3] - Mostrar carro específico ou todos os carros existentes
[4] - Sair
Insira a opção desejada: """

menuimp = """Selecione como você deseja visualizar a lista:
[1] - Mostrar todos os carros cadastrados
[2] - Mostrar parte específica da lista
Insira a opção desejada: """

#funções requisitadas
def cadastro():#função de cadastro, na main tava com erro pra gerar outros dicionario 
    if len(carros)<=49:
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
    else:
        print("Limite de veículos atingido!")

def search():
    termo = input("Digite marca, modelo, ano ou quantos km o veículo faz pro litro: ").upper()
    for carro in range(len(carros)):
        if termo == carros[carro]["marca"] or termo == carros[carro]["modelo"] or termo == str(carros[carro]["ano"]) or termo == str(carros[carro]["autonomia"]):
            print("Posição: ",carro+1,"   |   ","Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l") #eu queria colocar num print(f) mas por algum caralho de motivo da erro qnd eu faço isso
        
            
def imprimirtudo():
    for carro in range(len(carros)):
            print("Posição: ",carro+1,"   |   ","Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l")

def imprimirparte():
    posI = int(input("Insira a posição inicial da vizualização: "))
    posF = int(input("Insira a posição final da vizualização: "))
    for carro in range(posI-1, posF-1):
        print("Posição: ",carro+1,"   |   ","Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l")
    if posF > 49:
        print("Esse numero excede o tamanho da lista")

def imprimir():#talvez eu mude o nome dessa função pq esse nome é ruim demais
    impop = int(input(menuimp))
    if impop == 1:
        imprimirtudo()
    if impop == 2:
        imprimirparte()

#função principal do programa
op = 0
def main():
    op = int(input(menu))
    while op!= 4:
        if op == 1:
            cadastro()
        elif op == 2:
            search()
        elif op == 3:
            imprimir()
        else:
            print("Opção inválida!")
        op = int(input(menu))
    print("Obrigado por utilizar o sistema!")

#chama tudo
print(bem_vindo)
main()