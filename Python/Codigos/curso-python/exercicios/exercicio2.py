def cadastrar_pessoa(nome):
    try:
        print(" ---------------------------------- ")
        print("Iniciando o Cadastro de Pessoas...")

        nome.strip()
        nome.upper()

    except:
        print("Erro Inesperado, preencha os campos corretamente!")