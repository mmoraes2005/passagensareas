#----------------- Guilherme-----------------------

voos={}

def dados_voo():
    codigo=input('Código do voo:')
    org =input('Cidade de origem:')
    dest = input('Cidade de destino:')
    nes= int(input)('Número de escalas:')
    prç=float(input)('preço da passagem:')
    lugares=int(input)('Lugares disponíveis:')
    voos[codigo] ={'origem':org, 'destino':dest, 'escalas':nes, 'preço':prç, 'lugares':lugares}
    print('Voo cadastrado com sucesso!')

def busca_por_codigo():
    consulta = input('Digite o código do voo:')
    if consulta in voos:
        print(voos[consulta])
    else:
        print('Voo inexistente, digite o código correto')

def busca_por_origem():
    consulta2 =input('Digite a cidade de origem do voo:')
    cont =0
    for i in voos:
        if i['origem']==consulta2:
            print(f'Código:',i, ' Destino:',voos[i]['destino'], 'Preços: R$',voos[i]['preço'])
            cont=cont+1
        elif cont==0:
            print('Não há voos com este local de origem')

def busca_por_destino():
    consulta3 =input('Digite a cidade de destino do voo:')
    cont =0
    for i in voos:
        if i['destino']==consulta3:
            print(f'Código:',i, ' Origem:',voos[i]['origem'], 'Preços: R$',voos[i]['preço'])
            cont=cont+1
        elif cont==0:
            print('Não há voos com este local de destino')

-------------------------------------------------------------------------

usuarios = {}
programaRondo = True

def mostrarMenu():
    print("\n--- MENU ---")
    print("1. Cadastrar usúario")
    print("2. Listar usúario")
    print("3. Sair")

def cadastrarUsuario():
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
    print("-")
