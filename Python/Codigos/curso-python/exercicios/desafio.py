eleitores = []
opcao_voto = []

id_candidato = 0
id_eleitor = 0

def cadastrar_candidatos(id_candidato):

  qtd_candidato = 0

  qtd_candidato = int(input("Quantidade de candidatos pra eleição: "))

  while qtd_candidato < 1:
    print("Quantidade Inválida!")
    qtd_candidato = int(input("Quantidade de candidatos pra eleição: "))

  print("Cadastro de Candidatos\n")

  for cont in range(qtd_candidato):
  
    print("-------------------------------\n")

    nome = input("Nome do Candidato:\n")

    candidato = {
      "id": id_candidato,
      "nome": nome,
      "qtdVotos": 0,
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
  
  print("Cadastro(s) realizado(s) com sucesso!")

def cadastrar_eleitores(id_eleitor):

  qtd_eleitor = 0

  qtd_eleitor = int(input("Quantidade de eleitores para o cadastro: "))

  while qtd_eleitor < 1:
    print("Quantidade Inválida!")
    qtd_eleitor = int(input("Quantidade de eleitores para o cadastro: "))

  print("Cadastro de Eleitores\n")

  for cont in range(qtd_eleitor):
    print("-------------------------------\n")

    nome = input("Nome:\n")

    eleitor = {
      "id": id_eleitor,
      "nome": nome,
      "qtdVotos": 0,
    }
    eleitores.append(eleitor)

    id_eleitor += 1
  
  print("Cadastro(s) realizado(s) com sucesso!")

def visualizar_candidatos():
  try:
    for contador in opcao_voto:
      if contador['nome'] == 'Voto branco':
        break

      print("------------------------\n")
      print("ID: %s" % contador['id'])
      print("Nome: %s" % contador['nome'])

  except:
    print("Faliceu")

def visualizar_eleitores():
  try:
    print("------ Listando Eleitores ------\n")
    for contador in eleitores:
      print("-------------------------------\n")
      print("ID Eleitor: %s" % contador['id'])
      print("Nome Eleitor: %s" % contador['nome'])

  except:
    print("Erro Inesperado ao Listar Eleitores")

def votacao(eleitores, opcao_voto):
  
  print("------ Listando Eleitores ------\n")
  for contador in eleitores:
    print("-------------------------------\n")
    print("ID Eleitor: %s" % contador['id'])
    print("Nome Eleitor: %s" % contador['nome'])

  select_id_eleitor = int(input("Digite o ID do eleitor: "))

  for eleitor in eleitores:
    if select_id_eleitor == eleitor['id']:
      print(eleitor['nome'])
      print("Listando Candidatos\n") 
      m = 1
      for c in opcao_voto:
        
        print("------------------------\n")
        print(f"Nome do Candidato: {c['nome']} - Número: {m}")
        m += 1

      voto = int(input("Digite o Número do candidato: "))

      opcao_voto[voto-1]['qtdVotos'] += 1

      print(m)
      
      print("------------------------\n")

def apuracao(eleitores, opcao_voto):
  for c in opcao_voto:
    print("------------------------\n")
    print("Opção: %s" % c['nome'])
    print("Total de votos: %s" % c['qtdVotos'])
    print("------------------------\n")

  voto_branco = opcao_voto[-2]['qtdVotos']
  voto_nulo = opcao_voto[-1]['qtdVotos']

  aux = len(opcao_voto)

  percentual_branco = (voto_branco*100)/aux
  percentual_nulo = (voto_nulo*100)/aux

  print('Percentual de votos branco foi de "%0.2f"' % percentual_branco)
  print('Percentual de votos nulo foi de "%0.2f"' % percentual_nulo)

def menu():

  escolha = 1

  while escolha != 0:
    
    print(" ----------------- MENU ---------------- ")
    print(" NUMBER - 1 --- CADASTRAR CANDIDATO ---- ")
    print(" NUMBER - 2 --- CADASTRAR ELEITOR ------ ")
    print(" NUMBER - 3 --- VISUALIZAR CANDIDATO --- ")
    print(" NUMBER - 4 --- VISUALIZAR ELEITOR ----- ")
    print(" NUMBER - 5 --- VOTAR ------------------ ")
    print(" NUMBER - 6 --- APURAÇÃO --------------- ")
    print(" NUMBER - 0 --- SAIR ------------------- ")
    print(" --------------------------------------- ")

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