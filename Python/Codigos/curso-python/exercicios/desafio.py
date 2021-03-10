eleitores = []
opcao_voto = []

id_candidato = 1
id_eleitor = 1

def cadastrar_candidatos(id_candidato):
  try:

    print("\n\n ---------- INICIANDO CADASTRO DE CANDIDATOS ---------- \n")

    qtd_candidato = 0
    qtd_candidato = int(input("\nInsira quantos candidatos serão cadastrados: "))

    while qtd_candidato < 1:
      
      print("\n\n\n|------------------------------------------------------- |")
      print("\n|---------------- ERRO! Quantidade Inválida! --------------- |")
      print("\n|------------------------------------------------------- |\n\n\n")
    
      qtd_candidato = int(input("\nInsira quantos candidatos serão cadastrados: "))

    for cont in range(qtd_candidato):
    
      print("-------------------------------")

      nome = input("\nInsira o Nome: ")

      candidato = {
        "id": id_candidato,
        "nome": nome,
        "qtdVotos": 0,
        "voto": 0,
      }
      opcao_voto.append(candidato)

      id_candidato += 1

    branco = {
      "nome": "Voto branco",
      "qtdVotos": 0,
    }
    opcao_voto.append(branco)

    nulo = {
      "nome": "Voto nulo",
      "qtdVotos": 0,
    }
    opcao_voto.append(nulo)

    print("\n\n\n|------------------------------------------------------- |")
    print("\n|-- O(s) Cadastro(s) fo(ram) realizado(s) com sucesso!-- |")
    print("\n|------------------------------------------------------- |\n\n\n")

  except ValueError:
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|---------------- ERRO! Somente números! ----------------|")
    print("\n|------------------------------------------------------- |\n\n\n")
  
  except: 
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|----- ERRO! Não foi possivel realizar o cadastro! ----- |")
    print("\n|------------------------------------------------------- |\n\n\n")

def cadastrar_eleitores(id_eleitor):

  try:

    print("\n\n ---------- INICIANDO CADASTRO DE ELEITORES ---------- \n")

    qtd_eleitor = 0

    qtd_eleitor = int(input("\nInsira quantos eleitores serão cadastrados: "))

    while qtd_eleitor < 1:
      print("\n\n\n|------------------------------------------------------- |")
      print("\n|---------------- ERRO! Quantidade Inválida! --------------- |")
      print("\n|------------------------------------------------------- |\n\n\n")
      qtd_eleitor = int(input("\nInsira quantos eleitores serão cadastrados: "))

    for cont in range(qtd_eleitor):
      print("-------------------------------\n")

      nome = input("\nInsira o Nome:")

      eleitor = {
        "id": id_eleitor,
        "nome": nome,
        "qtdVotos": 0,
      }
      eleitores.append(eleitor)

      id_eleitor += 1
  
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|-- O(s) Cadastro(s) fo(ram) realizado(s) com sucesso!-- |")
    print("\n|------------------------------------------------------- |\n\n\n")

  except ValueError:
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|---------------- ERRO! Somente números! ----------------|")
    print("\n|------------------------------------------------------- |\n\n\n")
  
  except: 
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|----- ERRO! Não foi possivel realizar o cadastro! ----- |")
    print("\n|------------------------------------------------------- |\n\n\n")

def visualizar_candidatos():

  if len(opcao_voto) < 1:
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|---------------- ERRO! CADASTRE CANDIDATOS! ---------- |")
    print("\n|------------------------------------------------------- |\n\n\n")

  elif len(opcao_voto) > 1:
    for contador in opcao_voto:
      if contador['nome'] == 'Voto branco':
        break

      print(" ----------------------------- \n")
      print("Nome Candidato: %s" % contador['nome'])
      print("Número Candidato: %s" % contador['id'])
      
def visualizar_eleitores():
  if len(opcao_voto) < 1:
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|---------------- ERRO! CADASTRE ELEITORES! ------------ |")
    print("\n|------------------------------------------------------- |\n\n\n")

  elif len(opcao_voto) > 1:
    print("------ Listando Eleitores ------\n")
    for contador in eleitores:
      print("-------------------------------\n")

      print("Nome Eleitor: %s" % contador['nome'])
      print("Número Eleitor: %s" % contador['id'])

def votacao(eleitores, opcao_voto):
  
  if len(opcao_voto) < 1:
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|---------------- ERRO! CADASTRE CANDIDATOS! --------------- |")
    print("\n|------------------------------------------------------- |\n\n\n")

  elif len(eleitores) < 1:
    print("\n\n\n|------------------------------------------------------- |")
    print("\n|---------------- ERRO! CADASTRE ELEITORES! --------------- |")
    print("\n|------------------------------------------------------- |\n\n\n")

  elif len(opcao_voto) > 1 and len(eleitores) > 1:
    print("------ Listando Eleitores ------\n")
    for contador in eleitores:
      print("-------------------------------\n")
      print("Nome Eleitor: %s" % contador['nome'])
      print("Número Eleitor: %s" % contador['id'])

    select_id_eleitor = int(input("Digite o Número do eleitor: "))

    for eleitor in eleitores:
      if select_id_eleitor == eleitor['id']:
        if eleitor['voto'] == 1:
          print("\n\n\n|------------------------------------------------------- |")
          print("\n|-------------- ELEITOR JÁ REALIZOU A VOTAÇÃO! ------------- |")
          print("\n|------------------------------------------------------- |\n\n\n")

        elif eleitor['voto'] == 0:
          print("Listando Candidatos\n") 
          m = 1
          for c in opcao_voto:
            
            print("------------------------\n")
            print(f"Nome do Candidato: {c['nome']} - Número: {m}")
            m += 1

          voto = int(input("Digite o Número do candidato: "))

          opcao_voto[voto-1]['qtdVotos'] += 1
          opcao_voto[voto-1]['voto'] = 0

def apuracao(eleitores, opcao_voto):
  for c in opcao_voto:
    print("------------------------\n")
    print("Opção: %s" % c['nome'])
    print("Total de votos: %s" % c['qtdVotos'])
    print("------------------------\n")

  voto_branco = opcao_voto[-2]['qtdVotos']
  voto_nulo = opcao_voto[-1]['qtdVotos']

  aux = len(eleitores)

  percentual_branco = (voto_branco*100)/aux
  percentual_nulo = (voto_nulo*100)/aux

  print('Percentual de votos branco foi de "%0.2f"' % percentual_branco)
  print('Percentual de votos nulo foi de "%0.2f"' % percentual_nulo)

def menu():

  escolha = 1

  while escolha != 0:
    
    print(" | ----------------- MENU ---------------- | ")
    print(" | NUMBER - 1 --- CADASTRAR CANDIDATO ---- | ")
    print(" | NUMBER - 2 --- CADASTRAR ELEITOR ------ | ")
    print(" | NUMBER - 3 --- VISUALIZAR CANDIDATO --- | ")
    print(" | NUMBER - 4 --- VISUALIZAR ELEITOR ----- | ")
    print(" | NUMBER - 5 --- VOTAR ------------------ | ")
    print(" | NUMBER - 6 --- APURAÇÃO --------------- | ")
    print(" | NUMBER - 0 --- SAIR ------------------- | ")
    print(" | --------------------------------------- | ")

    escolha = int(input("Insira uma opção: "))  

    if escolha == 1:
      cadastrar_candidatos(id_candidato)

    elif escolha == 2:
      cadastrar_eleitores(id_eleitor)
      
    elif escolha == 3:
      visualizar_candidatos()

    elif escolha == 4:
      visualizar_eleitores()

    elif escolha == 5:
      votacao(eleitores, opcao_voto)  
    
    elif escolha == 6:
      apuracao(eleitores, opcao_voto) 

    elif escolha == 0:
      print("\nValeu Falou\n")
      break
  
    else:
      print("\nOpção Inválida!\n")

#cd languages/Python/Codigos/curso-python/exercicios
#python3
#from desafio import *
#menu()