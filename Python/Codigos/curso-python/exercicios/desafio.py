import math

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

    nome = input("Nome:\n")

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

  while qtd_candidato < 1:
    print("Quantidade Inválida!")
    qtd_candidato = int(input("Quantidade de eleitores para o cadastro: "))

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
    for contador in eleitores:

      print("------------------------\n")
      print("ID: %s" % contador['id'])
      print("Nome: %s" % contador['nome'])

  except:
    print("Faliceu")


def menu():
  escolha = 1

  while escolha != 0:
  
    print(" ----------------- MENU ------------------ ")
    print(" NUMBER - 1 --- CADASTRAR CANDIDATO ------ ")
    print(" NUMBER - 2 --- CADASTRAR ELEITOR -------- ")
    print(" NUMBER - 3 --- VISUALIZAR CANDIDATO ----- ")
    print(" NUMBER - 4 --- VISUALIZAR ELEITOR ----- ")

    print(" NUMBER - 5 --- VOTAR -------------------- ")
    print(" NUMBER - 6 --- APURAÇÃO ----------------- ")

    print(" NUMBER - 0 --- SAIR --------------------- ")
    print(" ----------------------------------------- ")

    escolha = int(input("Insira uma opção: "))  

    if escolha == 1:
      cadastrar_candidatos(id_candidato)

    elif escolha == 2:
      cadastrar_eleitores(id_eleitor)
      
    elif escolha == 3:
      visualizar_candidatos()

    elif escolha == 4:
      visualizar_eleitores()
    
    elif escolha == 0:
      print("\nValeu Falou\n")
      break
  
    else:
      print("\nOpção Inválida!\n")

#cd languages/Python/Codigos/curso-python/exercicios
#python3
#from desafio import *
#menu()