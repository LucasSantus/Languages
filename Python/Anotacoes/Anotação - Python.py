"""
	#
"""


	-------------------- LISTA DE ANOTAÇÕES - PYTHON --------------------

	|-------------------------------------------------------------------|
	|  OPERADOR | 			NOME			|  			AÇÂO			|
	|-----------|---------------------------|---------------------------|
	|	* 		|	Multiplicação			| 5 * 5 = 25				|
	|	/ 		|	Divisão					| 5 / 5 = 1					|
	|	- 		|	Subtração				| 5 - 5 = 0					|
	|	+ 		|	Adição					| 5 + 5 = 10				|
	|	**		|	Exponenciação			| 5 ** 5 = 3125				|
	|	// 		|	Parte Inteira			| 500 // 12 = 41 #seria 41.6|
	|	and		|	And                     |---------------------------|
	|	or 		|	Or 						|
	|	^ 		|	Or Exclusivo (Xor)		|
	|	% 		|	Módulo (MOD)			|
	|	not 	|	Negação					|
	|	> 		|	Maior Que				|
	|	>= 		|	Maior ou Igual Que		|
	|	< 		|	Menor Que				|
	|	<= 		|	Menor ou Igual Que		|
	|	== 		|	Igual á					|
	|	!= 		|	Diferente Que			|
	|	+= 		|	Mais Igual				|
	|	-= 		|	Menos Igual				|
	|	/= 		|	Dividido Igual			|
	|	*= 		|	Vezes Igual				|
	|	%= 		|	Módulo(MOD) Igual		|
	|	&& 		|	Condição "E"			|
	|	|| 		|	Condição "OU"			|
	|---------------------------------------|	

	-----------------------------------------

===================================================================================================

	== Algumas Funções ==



===================================================================================================

===================================================================================================

	== Inicio ==

#O Ínicio, Você Que Faz!

===================================================================================================

===================================================================================================

	== Input ==

variavel = Tipo(input("Texto"))

#Insere Valores as Variaveis.

===================================================================================================

===================================================================================================

	== Print ==

print("Texto")
print(""" Para Textos Enormes.. """)

#Outras Funções do "print".

print(sorted(lista)) #Irá plintar em ordem, ordenado.

print("="*5)
print("\n") #Quebra de Linha.
print("/"*3)

print("Soma = {:.2f}".format(num1 + num2)) = 7.34

print("Nome = {:<6}!".format(nome)) = lucas       !
print("Nome = {:>6}!".format(nome)) =        lucas!
print("Nome = {:^6}!".format(nome)) =     lucas   !
print("Nome = {:=^6}!".format(nome)) = ===lucas===!

----------------------------------------------------

print(f"Soma = {num1 + num2:.2f}") = 7.34

print(f"Nome = {nome:<6}!") = lucas       !
print(f"Nome = {nome:>6}!") =        lucas!
print(f"Nome = {nome:^6}!") =     lucas   !
print(f"Nome = {nome:=^6}!") = ===lucas===!




#Bastante Usado para Imprimir na Tela.

===================================================================================================

===================================================================================================

	== Format ==

#Há Duas Formas de Utilizar o Format

print("Mensagem {}".format(variavel))
print(f"Mensagem {variavel}")

#Utlizado para Formatar Textos.

===================================================================================================

===================================================================================================

	== Tipo Inteiro ==

int variavel = 106842156268354157278
variavel = int(input("Texto"))
print("Texto = {}".format(variavel))

#Números com Valores Inteiros.

===================================================================================================

===================================================================================================

	== Tipo Float ==

float variavel = 10.5956485781785717538
variavel = float(input("Texto"))
print("Texto = {}".format(variavel))

#Números com Ponto, Pequenos.

===================================================================================================

===================================================================================================

	== Tipo String ==

str variavel = "Texto"
variavel = str(input("Texto"))
print("Texto = {}".format(variavel))

#Possibilita Adicionar Textos a uma Variavel.

===================================================================================================

===================================================================================================

	== Tipo Bool ==

bool variavel = true or false
print(variavel)

#Utilizado para Variaveis Binárias(Booleandas)(True or False).

===================================================================================================

===================================================================================================

	== Estrutura de Repetição "For" ==

for nome in range (10, 1, -1): #Inicia no 10, Irá parar no 2, utiliza -1 para continuar
	#code

for nome in range (0, 10, 2): #Inicia no 0, Irá parar no 9, pulara 2 para continuar
	#code

for nome in range (5, 9): #Inicia no 5, Irá parar no 8
	#code

for nome in lista:
	print(f"{nome}...")

for c, a in enumerate(lista):
	print("{c} e {a}...")

for contador in range(0,5):
	lista.append(int(input("Adicione valores: ")))
	

#Bastante Usado Para Repetições.

===================================================================================================

===================================================================================================

	== Estrutura de Repetição "While" ==

while(variavel < 20):
	#code
	variavel += 1

#Executará o Loop Somente se for Verdadeira.

===================================================================================================

===================================================================================================

	== Módulos ==

#Há duas Maneiras de importar Módulos, importando inteira ou só uma função ou mais.

import biblioteca
from biblioteca import nome, nome

===================================================================================================

===================================================================================================

	== If / Else If / Else ==

#Utilizado para Questões de Decisão.

if (variavel == 1):
	#code 
elif (variavel == 2):
	#code 
else:
	#code 

----------------------------------------------------

print("Carro Novo" if tempo <= 3 else "Carro Velho") 

#Não Recomendado, Porém tem como Utilizar dessa Forma.

===================================================================================================

===================================================================================================

	== Módulo(MOD) ==

if(variavel % 3 == 0):
	print("É Divisivel por 3")
elif(variavel % 3 == 1):
	print("Não É Divisivel por 3")


#Utilizado para Descobrir o Resto.

===================================================================================================

===================================================================================================

	== Casting(CAST) ==

int num1 = 16
int num2 = 3
float resultado = (float) num1/num2
print("Resultado = {:2f}".format(resultado))

TELA: | 5.33 |

#Utilizado Para Mostrar o Real Valor de Uma Variavel.

===================================================================================================

===================================================================================================

	== Textos ==
	   	
frase =	| C| U| R| S| O|  | E| M|  | V| I| D| E| O|  | P| Y| T| H| O| N|
	 	  0	 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20	

frase[9] = "V"
frase[:5] = "CURSO"
frase[15:] = "PYTHON"
frase[15::2] = "PTO"
frase[1:5] = "URSO"
frase[9:13] = "VIDE"

---------------------------------------------------------------------------------------------------

divid = frase.split()							#Divide o Texto em partes, formando um tipo de lista.

		 _______0_______   __1__    _______2______    ________3________
divid =	| C| U| R| S| O|  | E| M|  | V| I| D| E| O|  | P| Y| T| H| O| N|
	 	| 0	 1  2  3  4|  | 0  1|  | 0  1  2  3  4|  | 0  1  2  3  4  5|

print(divid[2][3]) = "E" #Irá mostrar a letra da coluna 2, número 3.

"-".join(frase) = | C| U| R| S| O|-| E| M|-| V| I| D| E| O|-| P| Y| T| H| O| N| 	#No caso, iria juntar em uma cadeia de caracteres novamente, porém com "-" em suas configurações.

---------------------------------------------------------------------------------------------------

frase.count("O",0,14) = 1  						#Quantos "O" existem de 0 a 13.
frase.find("DEO") = 11  						#Mostra a numeração de quando inicia o 1º "DEO".
frase.find("ANDROID") = -1  					#Mostra -1, caso a palavra não exista no texto.
frase.replace("PYTHON", "ANDROID")  			#Substituirá "PYTHON" por "ANDROID".
frase.upper() = "CURSO EM VIDEO PYTHON"  		#Deixa tudo em Maiusculo.
frase.lower() = "curso em video python"  		#Deixa tudo em Minusculo.
frase.capitalize() = "Curso em video python"  	#Deixa apenas a 1ª Palavra Maisculo.
frase.title() = "Curso Em Video Python"  		#Deixa Todas as 1ª's Letras das Palavras em Maiusculas.
"CURSO"	in frase = true

---------------------------------------------------------------------------------------------------

print(len(frase.strip())) = 21  				#Lê o tamanho da frase.
print(frase.lower().find("video")) = 9  		#Deixa o Texto todo em Minusculo, logo após verifica onde começa o "video".

frase.lstrip() = |X|X|X| A| P| R| E| N| D| A| | P| Y| T| H| O| N| | | | 	#Remove todos os espaços inuteis da esquerda.
frase.rstrip() = | | | | A| P| R| E| N| D| A| | P| Y| T| H| O| N|X|X|X| 	#Remove todos os espaços inuteis da direita.
frase.strip() =  |X|X|X| A| P| R| E| N| D| A| | P| Y| T| H| O| N|X|X|X| 	#Remove todos os espaços inuteis.
					   | A| P| R| E| N| D| A| | P| Y| T| H| O| N|

===================================================================================================

===================================================================================================

	== Random ==

import Random

lista = []

random.choice(lista)		#Escolhe um item aleatório na lista.
random.shuffle(lista) 		#Embaralha a lista.

===================================================================================================

===================================================================================================

	== Código ANSI ==

	|----------- Style -------|
	|---|---------------------|
	| 0 |  NONE				  |
	| 1 |  NEGRITO			  |
	| 4 |  SUBLINHADO		  |
	| 7 |  INVERTER(NEGATIVO) |
	|---|---------------------|


	|-------------------------|
	|Text| ---- Cor ---- |Back|
	|----|---------------|----|
	| 30 |  BRANCO		 | 40 |
	| 31 |  VERMELHO	 | 41 |
	| 32 |  VERDE		 | 42 |
	| 33 |  AMARELO      | 43 |
	| 34 |  AZUL		 | 44 |
	| 35 |  LILÁS		 | 45 |
	| 36 |  AZUL CLARO	 | 46 |
	| 37 |  CINZA 		 | 47 |
	|----|---------------|----|

print("\033[0;32mOlá Mundo!") #Cor Verde Adicionada.

===================================================================================================

===================================================================================================

	== Lista ==

lista = [
			5,
			8,
			2,
			0
		]



#Utilizado Para Receber Valores.

===================================================================================================

===================================================================================================

	== Dicionário ==

cores = {
			"limpa":"\033[m",
			"azul":"\033[34m",
			"amarelo":"\033[33m",
			"verde":"\033[32m",
			"negativo":"\033[7;30m"
		}

print("{}Olá Mundo!".format(cores["azul"]))

===================================================================================================

===================================================================================================

	== Tupla ==

lanche = (
	"Hamburguer", 
	"Suco", 
	"Pizza", 
	"Pudim"
	)

for comida in lanche:
	print("Alimento: {}".format(comida))

#Pode receber dados de tipos diferentes em uma tupla.
#Tuplas São Imutaveis!

===================================================================================================

===================================================================================================

	== Break ==

break

#Utlizado para Interromper algo.

===================================================================================================

===================================================================================================

	