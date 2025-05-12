voos = {}            # chave: código do voo, valor: dict com dados do voo
passageiros = {}     # chave: CPF, valor: dict com nome e telefone
passagens = {}       # chave: código do voo, valor: lista de CPFs

# ---------- PARTE 1: CADASTRO E CONSULTAS ----------
def cadastrar_voo():
    codigo = input("Código do voo: ")
    origem = input("Cidade de origem: ")
    destino = input("Cidade de destino: ")
    escalas = int(input("Número de escalas: "))
    preco = float(input("Preço da passagem: "))
    lugares = int(input("Quantidade de lugares: "))
    
    voos[codigo] = {
        "origem": origem,
        "destino": destino,
        "escalas": escalas,
        "preco": preco,
        "lugares": lugares
    }
    passagens[codigo] = []
    print("Voo cadastrado com sucesso!")

def consultar_voo_por_codigo():
    codigo = input("Código do voo: ")
    if codigo in voos:
        print(voos[codigo])
    else:
        print("Voo não encontrado.")

def consultar_voos_por_origem():
    origem = input("Cidade de origem: ")
    achou = False
    for codigo, voo in voos.items():
        if voo["origem"] == origem:
            print(f"Código: {codigo}, Destino: {voo['destino']}, Preço: R${voo['preco']}")
            achou = True
    if not achou:
        print("Nenhum voo encontrado para essa origem.")

def consultar_voos_por_destino():
    destino = input("Cidade de destino: ")
    achou = False
    for codigo, voo in voos.items():
        if voo["destino"] == destino:
            print(f"Código: {codigo}, Origem: {voo['origem']}, Preço: R${voo['preco']}")
            achou = True
    if not achou:
        print("Nenhum voo encontrado para esse destino.")

# ---------- PARTE 2: VENDA E CANCELAMENTO ----------
def vender_passagem():
    cpf = input("CPF do passageiro: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    codigo = input("Código do voo: ")

    if codigo in voos:
        if voos[codigo]["lugares"] == 0:
            print("Voo lotado.")
            return
        if cpf in passageiros:
            if passageiros[cpf]["nome"] != nome:
                print("CPF já cadastrado com nome diferente.")
                return

        passageiros[cpf] = {"nome": nome, "telefone": telefone}
        passagens[codigo].append(cpf)
        voos[codigo]["lugares"] -= 1
        print("Passagem vendida com sucesso.")
    else:
        print("Voo não encontrado.")

def cancelar_passagem():
    cpf = input("CPF: ")
    codigo = input("Código do voo: ")

    if codigo in voos:
        if cpf in passagens[codigo]:
            passagens[codigo].remove(cpf)
            voos[codigo]["lugares"] += 1
            print("Passagem cancelada.")
        else:
            print("Passagem não encontrada para este CPF no voo.")
    else:
        print("Voo não encontrado.")

# ---------- PARTE 3: INTEGRAÇÃO E TRATAMENTO DE ERROS ----------
def consultar_menor_escala():
    origem = input("Cidade de origem: ")
    destino = input("Cidade de destino: ")
    menor_escala = None
    codigo_menor = None
    for codigo, voo in voos.items():
        if voo["origem"] == origem and voo["destino"] == destino:
            if menor_escala is None or voo["escalas"] < menor_escala:
                menor_escala = voo["escalas"]
                codigo_menor = codigo
    if codigo_menor:
        print(f"Voo {codigo_menor} tem a menor quantidade de escalas ({menor_escala}).")
    else:
        print("Nenhum voo encontrado para esses critérios.")

def listar_passageiros_voo():
    codigo = input("Código do voo: ")
    if codigo in passagens:
        lista = passagens[codigo]
        if len(lista) > 0:
            print(f"Passageiros do voo {codigo}:")
            for cpf in lista:
                print(f"- {cpf}: {passageiros[cpf]['nome']}")
        else:
            print("Ainda não há passageiros neste voo.")
        print(f"Lugares disponíveis: {voos[codigo]['lugares']}")
    else:
        print("Voo não encontrado.")

def menu():
    continuar = True
    while continuar:
        print("\n----- MENU -----")
        print("1. Cadastrar voo")
        print("2. Consultar voo por código")
        print("3. Consultar voos por origem")
        print("4. Consultar voos por destino")
        print("5. Voo com menor escala")
        print("6. Vender passagem")
        print("7. Cancelar passagem")
        print("8. Listar passageiros de um voo")
        print("9. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_voo()
        elif opcao == "2":
            consultar_voo_por_codigo()
        elif opcao == "3":
            consultar_voos_por_origem()
        elif opcao == "4":
            consultar_voos_por_destino()
        elif opcao == "5":
            consultar_menor_escala()
        elif opcao == "6":
            vender_passagem()
        elif opcao == "7":
            cancelar_passagem()
        elif opcao == "8":
            listar_passageiros_voo()
        elif opcao == "9":
            print("Encerrando o sistema.")
            continuar = False
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()