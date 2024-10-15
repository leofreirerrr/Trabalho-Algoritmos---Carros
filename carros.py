carros = []

#parte estética
bem_vindo = """======================================================BEM-VINDO=========================================================="""
divisaoli = """==========================================================LISTA==========================================================="""
divisao = """=========================================================================================================================="""

#menus
menu = """=> O que deseja fazer agr?
[1] - Cadastrar um novo veículo 
[2] - Buscar por algum veículo existente
[3] - Mostrar carro específico ou todos os carros existentes
[4] - Sair
Insira a opção desejada: """

menuimp = """=> Selecione como você deseja visualizar a lista:
[1] - Mostrar todos os carros cadastrados
[2] - Mostrar parte específica da lista
Insira a opção desejada: """

#funções requisitadas
def cadastro():#função de cadastro: solicito todos os campos para o usuario e adiciono o dicionario dentro da lista carros
    if len(carros)<=49:
        marca = str(input("Insira a marca do carro: ")).upper()
        modelo =str(input("Insira modelo do carro: ")).upper()
        ano = int(input("Insira o ano-modelo do veículo: "))
        aut = float(input("Insira quantos km o veículo faz por litro na cidade: "))
        carros.append({
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "autonomia": aut
        })
        print("\n=>Cadastro concluído!")
    else:
        print("Limite de veículos atingido!")

def search():#função de pesquisa: eu transformo todos os tipos registrados no dicionario em string e faço a comparação
    encontrou = False
    termo = input("=> Digite marca, modelo, ano ou quantos km o veículo faz por litro: ").upper()
    print(divisaoli)
    for carro in range(len(carros)):
        if termo == carros[carro]["marca"] or termo == carros[carro]["modelo"] or termo == str(carros[carro]["ano"]) or termo == str(carros[carro]["autonomia"]):
            print("Posição: ",carro+1,"   |   ","Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l")
            encontrou = True
    if encontrou == False:
        print("Elemento não encontrado")
        
def mostrartudo():#divisão da função mostrar
    print(divisaoli)
    for carro in range(len(carros)):
            print("Posição: ",carro+1,"   |   ","Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l")

def mostrarparte():#outra divisão da função mostrar
    posI = int(input("Insira a posição inicial da vizualização: "))
    posF = int(input("Insira a posição final da vizualização: "))
    print(divisaoli)
    for carro in range(posI-1, posF):
        print("Posição: ",carro+1,"   |   ","Marca: ",carros[carro]['marca'], "   |   ","Modelo: ", carros[carro]['modelo'], "   |   ", "Ano-modelo: ",carros[carro]['ano'], "   |   ","Autonomia(cidade): ",  carros[carro]['autonomia'], "km/l")
    if posF > 50:
        print("Esse numero excede o tamanho da lista")

def mostrar():#separei a função em dois para ficar mais facil de trabalhar
    impop = int(input(menuimp))
    if impop == 1:
        mostrartudo()
    if impop == 2:
        mostrarparte()

def main():#função principal do programa
    op = int(input(menu))
    while op!= 4:
        print(divisao)
        if op == 1:
            cadastro()
            print(divisao)
        elif op == 2:
            search()
            print(divisao)
        elif op == 3:
            mostrar()
            print(divisao)
        else:
            print("Opção inválida!")
        op = int(input(menu))
    print(divisao)
    print("=> Obrigado por utilizar o sistema!")

#chama tudo
print(bem_vindo)
main()