carros = []
carro = {}
termo  = ""
op = 0
aut = []

print('='*70)
print('\t'*3,"SISTEMA DE CADASTRO")
print('='*70)
print("[1] - Cadastrar um novo veículo \n[2] - Buscar por algum veículo existente\n[3] - Mostrar todos os veículos existentes\n[4] - Sair")
opcao = int(input("Selecione o número da opção desejada: "))

while opcao >=1 and opcao<4:
    if opcao == 1:
        n = int(input("\nQuantos veículos você deseja cadastrar? "))
        for i in range(n):
            carro["marca"] = str(input(f"Insira a marca do {i+1}º veículo: ")).lower()
            carro["modelo"] = str(input(f"Insira o modelo do veículo: ")).lower()
            carro["ano"] = int(input("Insira o ano-modelo do veículo: "))
            carro["autonomia"] = float(input("Insira quantos km o veículo faz por litro: "))
            carros.append(carro)
        print(f"Cadastro Concluído!")
    print('='*70)
    opcao = int(input("O que deseja fazer agr?\n[1] - Cadastrar um novo veículo \n[2] - Buscar por algum veículo existente\n[3] - Mostrar carro específico ou todos os carros existentes\n[4] - Sair\nInsira a opção desejada: "))
    print('='*70)
    
    if opcao == 2:
        op = int(input("Selecione por qual termo você deseja fazer a pesquisa\n[1] - Marca\n[2] - Modelo\n[3] - Ano\n[4] - Autonomia\n[5] - \nInsira a opção desejada: "))
        if op == 1:
            termo  = str(input("\nDigite o nome da marca do veículo que você deseja: ")).lower()
            if termo == carros[i]["marca"]:
                print(f"Os veículos da marca {termo} presentes no sistema são:")
                for i in range(len(carros)):
                    print('modelo:',carros[i]["modelo"], '\t', '\tano:',carros[i]["ano"])#ajustar os termos
            else:
                print("Não existem veículos com essa descrição")
        if op == 2:
            termo  = str(input("\nDigite o modelo do veículo que você deseja: ")).lower()
            if termo == carros[i]["modelo"]:
                print(f"Os veículos do modelo {termo} presentes no sistema são:")
                for i in range(len(carros)):
                    print(carros[i]["ano"], carros[i]["autonomia"])#ajustar os termos depois
            else:
                print("Não existem veículos com essa descrição")
        if op == 3:
            termo  = int(input("\nDigite o ano-modelo do veículo que você deseja: "))
            if termo == carros[i]["ano"]:
                print(f"Os veículos dd modelo {termo} presentes no sistema são:")
                for i in range(len(carros)):
                    print(carros[i]["marca"], carros[i]["modelo"],carros[i]["ano"])#ajustar os termos depois
            else:
                print("Não existem veículos com essa descrição")
        if op == 4:
            termo  = float(input("\nDigite o ano-modelo do veículo que você deseja: "))
            if termo == carros[i]["ano"]:
                print(f"Os veículos da marca {termo} presentes no sistema sãdao:")
                for i in range(len(carros)):
                    print(carros[i]["marca"], carros[i]["modelo"],carros[i]["autonomia"])#ajustar os termos depois 
    if opcao == 3:
        print('\t'*3,"LISTA COMPLETA\n")
        for i in range(len(carros)):
            print('marca:', carros[i]["marca"],'\t','modelo:',carros[i]["modelo"], '\t', 'ano:',carros[i]["ano"],'\t','autonomia:',carros[i]["autonomia"])

if opcao == 4:
        print("Obrigado por utilizar o sistema!")
        