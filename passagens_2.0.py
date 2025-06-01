voos = {}
passageiros = {}
passagens_por_voo = {}

def dados_voo():
    codigo = input('Código do voo: ')
    origem = input('Cidade de origem: ')
    destino = input('Cidade de destino: ')
    escalas = int(input('Número de escalas: '))
    preco = float(input('Preço da passagem: '))
    lugares = int(input('Lugares disponíveis: '))
    
    voos[codigo] = {
        'origem': origem,
        'destino': destino,
        'escalas': escalas,
        'preco': preco,
        'lugares': lugares
    }
    passagens_por_voo[codigo] = []
    print('Voo cadastrado com sucesso!')

def busca_por_codigo():
    codigo = input('Digite o código do voo: ')
    if codigo in voos:
        info = voos[codigo]
        print(f"\nCódigo: {codigo}")
        print(f"Origem: {info['origem']}")
        print(f"Destino: {info['destino']}")
        print(f"Escalas: {info['escalas']}")
        print(f"Preço: R${info['preco']:.2f}")
        print(f"Lugares disponíveis: {info['lugares']}")
    else:
        print('Voo inexistente!')

def busca_por_origem():
    origem = input('Digite a cidade de origem: ')
    encontrados = False
    
    for codigo, info in voos.items():
        if info['origem'].lower() == origem.lower() and info['lugares'] > 0:
            print(f"\nCódigo: {codigo}")
            print(f"Destino: {info['destino']}")
            print(f"Preço: R${info['preco']:.2f}")
            encontrados = True
    
    if not encontrados:
        print('Nenhum voo encontrado para esta origem')

def busca_por_destino():
    destino = input('Digite a cidade de destino: ')
    encontrados = False
    
    for codigo, info in voos.items():
        if info['destino'].lower() == destino.lower() and info['lugares'] > 0:
            print(f"\nCódigo: {codigo}")
            print(f"Origem: {info['origem']}")
            print(f"Preço: R${info['preco']:.2f}")
            encontrados = True
    
    if not encontrados:
        print('Nenhum voo encontrado para este destino')

def menor_escala():
    origem = input('Origem: ')
    destino = input('Destino: ')
    melhor_voo = None
    
    for codigo, info in voos.items():
        if (info['origem'].lower() == origem.lower() and 
            info['destino'].lower() == destino.lower() and
            info['lugares'] > 0):
            
            if melhor_voo is None or info['escalas'] < voos[melhor_voo]['escalas']:
                melhor_voo = codigo
    
    if melhor_voo:
        info = voos[melhor_voo]
        print(f"\nVoo com menor escala: {melhor_voo}")
        print(f"Escalas: {info['escalas']}")
        print(f"Preço: R${info['preco']:.2f}")
    else:
        print("Não há voos disponíveis para este trajeto")

def listar_passageiros():
    codigo = input('Código do voo: ')
    
    if codigo not in voos:
        print("Voo inexistente!")
        return
    
    if not passagens_por_voo[codigo]:
        print("Não há passageiros neste voo")
        return
    
    print(f"\nPassageiros do voo {codigo}:")
    for cpf in passagens_por_voo[codigo]:
        print(f"- {passageiros[cpf]['nome']} (CPF: {cpf})")
    
    print(f"\nLugares disponíveis: {voos[codigo]['lugares']}")

def vender_passagem():
    codigo = input('Código do voo: ')
    
    if codigo not in voos:
        print("Voo inexistente!")
        return
    
    if voos[codigo]['lugares'] <= 0:
        print("Voo lotado!")
        return
    
    nome = input('Nome do passageiro: ')
    cpf = input('CPF: ')
    telefone = input('Telefone: ')
    
    if cpf in passageiros and passageiros[cpf]['nome'] != nome:
        print("Erro: CPF já cadastrado com outro nome!")
        return
    
    passageiros[cpf] = {'nome': nome, 'telefone': telefone}
    passagens_por_voo[codigo].append(cpf)
    voos[codigo]['lugares'] -= 1
    print("Passagem vendida com sucesso!")

def cancelar_passagem():
    codigo = input('Código do voo: ')
    
    if codigo not in voos:
        print("Voo inexistente!")
        return
    
    cpf = input('CPF do passageiro: ')
    
    if cpf not in passagens_por_voo[codigo]:
        print("Passageiro não encontrado neste voo!")
        return
    
    passagens_por_voo[codigo].remove(cpf)
    voos[codigo]['lugares'] += 1
    print("Passagem cancelada com sucesso!")

def menu():
    executando = True
    while executando:
        print("\n--- SISTEMA DE PASSAGENS AÉREAS ---")
        print("1. Cadastrar voo")
        print("2. Consultar voo por código")
        print("3. Consultar voos por origem")
        print("4. Consultar voos por destino")
        print("5. Encontrar voo com menor escala")
        print("6. Listar passageiros de um voo")
        print("7. comprar passagem")
        print("8. Cancelar passagem")
        print("0. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            dados_voo()
        elif opcao == '2':
            busca_por_codigo()
        elif opcao == '3':
            busca_por_origem()
        elif opcao == '4':
            busca_por_destino()
        elif opcao == '5':
            menor_escala()
        elif opcao == '6':
            listar_passageiros()
        elif opcao == '7':
            vender_passagem()
        elif opcao == '8':
            cancelar_passagem()
        elif opcao == '0':
            print("Sistema encerrado!")
            executando = False
        else:
            print("Opção inválida!")

menu()