# DESAFIO
# Fechar possiveis brechas pra erro.
# Adicionar o nome ao eleitor.
# Adicionar um menu se a pessoa quer cadastrar um candidato ou eleitor
# No menu tbm tem a opção de votar ou ver apuração de votos
# Dica coloque um campo no eleitor pra poder indicar quem vai votar

opcaoVoto = []
eleitores = 0
qtdCandidatos = 0

id_candidato = 0
id_eleitor = 0

def eleicao():
    try:
        qtdCandidatos = int(input("Quantidade de candidatos pra eleição: "))

        while qtdCandidatos < 1:
            if qtdCandidatos < 1:
                print("Quantidade Inválida!")
                qtdCandidatos = int(input("Quantidade de candidatos pra eleição: "))

        cadastrar_candidatos(qtdCandidatos)

        print("------------------------\n")
        eleitores = int(input("Quantidade de eleitores para votar: "))

        for e in range(eleitores):
            cont = 1
            print("Eleitor - %s" % (e+1))
            for o in opcaoVoto:
                print("Pra votar '%s' digite: %s" % (o['nome'], cont))
                cont += 1

            voto = int(input("Digite sua opçao: "))
            opcaoVoto[voto-1]['qtdVotos'] += 1
            print("------------------------\n")

        for c in opcaoVoto:
            print("------------------------\n")
            print("Opção: %s" % c['nome'])
            print("Total de votos: %s" % c['qtdVotos'])
            print("------------------------\n")

        votoBranco = opcaoVoto[-2]['qtdVotos']
        votoNulo = opcaoVoto[-1]['qtdVotos']

        percentualBranco = (votoBranco*100)/eleitores
        percentualNulo = (votoNulo*100)/eleitores
        print('Percentual de votos branco foi de "%0.2f"' % percentualBranco)
        print('Percentual de votos nulo foi de "%0.2f"' % percentualNulo)

    except:
        print("Faliceu")

def cadastrar_eleitores(qtdEleitores):

    for cont in range(qtdEleitores):
        nome = input("Nome do eleitor: ")
        print("------------------------\n")
        candidato = {
            "id": id_candidato,
            "nome": nome,
            "qtdVotos": 0,
        }
        opcaoVoto.append(candidato)

    branco = {
        "nome": "Voto branco",
        "qtdVotos": 0,
    }
    opcaoVoto.append(branco)

    nulo = {
        "nome": "Voto nulo",
        "qtdVotos": 0,
    }
    opcaoVoto.append(nulo)

def votar():
    print("Selecione o Eleitor para votação: ")

def cadastrar_candidatos(qtdCandidatos):

    for cont in range(qtdCandidatos):
        print("------------------------\n")

        nome = input("Nome:\n")

        candidato = {
            "id": id_candidato,
            "nome": nome,
            "qtdVotos": 0,
        }

        opcaoVoto.append(candidato)

    branco = {
        "nome": "Voto branco",
        "qtdVotos": 0,
    }
    opcaoVoto.append(branco)

    nulo = {
        "nome": "Voto nulo",
        "qtdVotos": 0,
    }
    opcaoVoto.append(nulo)

#def apuracao():

def menu():
    print("MENU")