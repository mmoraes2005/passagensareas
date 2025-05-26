voos={}
dic_passageiros={}
dic_passagens={} 

def dados_voo(): # Função para inserir
    codigo=input('Código do voo:')
    org =input('Cidade de origem:')
    dest = input('Cidade de destino:')
    nes= int(input)('Número de escalas:')
    prç=float(input)('preço da passagem:')
    lugares=int(input)('Lugares disponíveis:')
    voos[codigo] ={'origem':org, 'destino':dest, 'escalas':nes, 'preço':prç, 'lugares':lugares}
    dic_passagens[codigo]=[]
    print('Voo cadastrado com sucesso!')

def busca_por_codigo(): # Função para buscar o voo pelo código
    consulta = input('Digite o código do voo:')
    if consulta in voos:
        print(voos[consulta])
    else:
        print('Voo inexistente, digite o código correto')

def busca_por_origem(): # Função para buscar o voo pela cidade de origem
    consulta2 =input('Digite a cidade de origem do voo:')
    cont =0
    for i in voos:
        if i['origem']==consulta2:
            print(f'Código:',i, ' Destino:',voos[i]['destino'], 'Preços: R$',voos[i]['preço'])
            cont=cont+1
        elif cont==0:
            print('Não há voos com este local de origem')

def busca_por_destino(): # Função para buscar o voo pelo destino
    consulta3 =input('Digite a cidade de destino do voo:')
    cont =0
    for i in voos:
        if i['destino']==consulta3:
            print(f'Código:',i, ' Origem:',voos[i]['origem'], 'Preços: R$',voos[i]['preço'])
            cont=cont+1
        elif cont==0:
            print('Não há voos com este local de destino')

def comprapassagem(): # Comprar uma passagem de algum voo
    codigo=input(f'Digite o código do voo:')
    nome=input(f'Seu nome:')
    cpf=input(f'Seu CPF:')
    if codigo in voos: 
        if voos[codigo]["lugares"] == 0:
            print(f'Este voo está lotado.') # Se o codigo existir em voos, e não tiver lugar está lotado
            return
        dic_passageiros[cpf]={"nome":nome}
        dic_passagens[codigo].append(cpf)
        voos[codigo]["lugares"] -=1
        print(f'A passagem foi vendida!')
    else:
        print(f'O voo não existe.')
usuarios = {}
programaRondo = True

def cancelarpassagem(): # Cancelar uma passagem
    codigo=input(f'Digite o código:')
    cpf=input(f'Digite o cpf:')
    if codigo in voos:
        if cpf in dic_passagens[codigo]:
            dic_passagens[codigo].remove(cpf)
            voos[codigo]["lugares"] += 1
            print(f'Sua passagem foi cancelada!') # Se o codigo existir no voos, e se o cpf estiver nesse voo ele remove esse cpf e adiciona um lugar
        else:
            print(f'CPF errado ou não existe.')
    else:
        print(f'Código errado ou não existe.')

def mostrarMenu(): # Função pra mostrar o menu
    print("\n--- MENU ---")
    print("1. Cadastrar usúario")
    print("2. Listar usúario")
    print("3. Sair")

def cadastrarUsuario(): # Função para cadastrar o cpf do usuario (Verificando se está certo)
    cpf = input("Digite o CPF: ")
    
    if len(cpf) != 11 or not cpf.isdigit():
        print("Erro: CPF deve ter 11 digitos numéricos")
        return

    if cpf in usuarios:
        print("ERRO: CPF ja possiu um cadastro")
    
    nome = input("Nome: ")
    if not nome: 
        print("ERRO: Nome não pode estar vazio")
        return
    
    usuarios[cpf] = nome 
    print("Cadastro realizado com sucesso!")

def listaUsuario(): 
    if not usuarios:
        print("Nenhum usuário cadastrado")
        return
    
    print("--- LISTAGEM ---")
    for cpf, nome in usuarios.items():
        print(f"CPF:{cpf} | Nome:{nome}")

def sair():
    global programaRondo
    programaRondo = False 
    print("Saindo do sistema")

acoes = {
    '1': cadastrarUsuario,
    '2': listaUsuario,
    '3': sair
}

while programaRondo:
    mostrarMenu()
    opcao = input("Opção: ")

    if opcao in acoes: 
        acoes[opcao]()
    else:
        print("Opção invalida! Digite 1, 2 ou 3")