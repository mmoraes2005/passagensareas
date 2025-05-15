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