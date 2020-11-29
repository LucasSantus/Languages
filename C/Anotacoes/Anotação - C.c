/*
	//
*/

	-------- LISTA DE ANOTAÇÕES - C --------

	|---------------------------------------|
	|  OPERADOR | 	AÇÃO(Nome)				|
	|-----------|---------------------------|
	|	>> 		|	Deslocamento a Direita  |
	|	<< 		|	Deslocamento a Esquerda |
	|	& 		|	And                     |
	|	| 		|	Or 						|
	|	~ 		|	Complemento (Not)       |
	|	^ 		|	Or Exclusivo (Xor)		|
	|	--		|	Declemento				|
	|	++ 		|	Inclemento				|
	|	- 		|	Subtração				|
	|	+ 		|	Adição					|
	|	% 		|	Módulo (MOD)			|
	|	* 		|	Multiplicação			|
	|	/ 		|	Divisão					|
	|	! 		|	Negação					|
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

===================================================================================================

	== Inicio ==

#include <stdio.h>
#include <stdlib.h>

int main(void){
	//code 
	return 0;
}

//Estrutura Padrão.

===================================================================================================

===================================================================================================

	== Scanf ==

scanf("%Tipo", &variavel); 

//Insere Valores as Variaveis.

===================================================================================================

===================================================================================================

	== Fgets ==

fgets(variavel,tamanho,stdin); 

//Insere Textos para Strings.

===================================================================================================

===================================================================================================

	== Printf ==

printf("Mensagem"); 

//Bastante Usado para Imprimir na Tela.

===================================================================================================

===================================================================================================

	== Tipo Inteiro ==

int variavel = 10;
scanf("%i", &variavel);
printf("%i", variavel);

//Números com Valores Inteiros.

===================================================================================================

===================================================================================================

	== Tipo Float ==

float variavel = 10.59;
scanf("%f", &variavel);
printf("%f", variavel);

//Números com Ponto, Pequenos.

===================================================================================================

===================================================================================================

	== Tipo Char ==

char variavel = "Letras";
scanf("%c", &variavel);
printf("%c", variavel);

//Adiciona Letras em uma Variavel, Caso Deseje Adicionar Textos, Seria Recomendado usar Strings.

===================================================================================================

===================================================================================================

	== Tipo String ==

#include <string.h>

char variavel = "Texto";
fgets(variavel, 50, stdin); //O Tamanho Você Escolhe!
printf("%s", variavel);

//Possibilita Adicionar Textos a uma Variavel.

===================================================================================================

===================================================================================================

	== Tipo Double ==

double variavel = 17.68456975;
scanf("%f", &variavel);
printf("%lf", variavel);

//Números com Ponto, Grandes.

===================================================================================================

===================================================================================================

	== Tipo Long ==

long int variavel = 176845696724575;
long double variavel = 17.64325468456975;
scanf("%Tipo", &variavel);
printf("%Tipo", variavel);

//Possibilita Adicionar Números Maiores as Variaveis.

===================================================================================================

===================================================================================================

	== Tipo Bool ==

#include <stdbool.h>

bool variavel = true or false;
printf(variavel);

//Utilizado para Variaveis Binárias(Booleandas)(True or False).

===================================================================================================

===================================================================================================

	== Constantes ==

//Há Duas Formas de Usar Variaveis Constantes em C, Siga os Exemplos Abaixo:

const int variavel = 17;				|	#define variavel 17
const float variavel = 1.27;			|	#define variavel 1,27
const double variavel = 11.876514278;	|	#define variavel 11,876514278

//Possibilita o Valor da Variavel a Nunca Mudar Durante a Execução.

===================================================================================================

===================================================================================================

	== Unsigned ==

unsigned int variavel = 17;				
unsigned float variavel = 1.27;			
unsigned double variavel = 11.876514278;

//Usados para Receber Somente Valores Positivos

===================================================================================================

===================================================================================================

	== Estrutura de Repetição "For" ==

for (int i = 0; i < TamanhoMaximo; ++i)
{
	//code
}

//Bastante Usado Para Repetições.

===================================================================================================

===================================================================================================

	== Estrutura de Repetição "While" ==

while(variavel != 0){
	//code
	//executará!!
}

//Executará o Loop Somente se for Verdadeira.

===================================================================================================

===================================================================================================

	== Estrutura de Repetição " Do While" ==

do
{
	//code 
	//não executará
} while (variavel != 0);

//Executará o Loop Somente se for Falso.

===================================================================================================

===================================================================================================

	== Switch ==

switch(variavel){
	case valor:
		//code
		break;
	case valor:
		//code
		break;
	default:
		//code
		break;
}

//Utilizado para Questões de Decisão.

===================================================================================================

===================================================================================================

	== If / Else If / Else ==

if (variavel == 1){
	//code 
}
else if (variavel == 2){
	//code 
}
else{
	//code 
}

//Utilizado para Questões de Decisão.

===================================================================================================

===================================================================================================

	== Operador Ternário "?:" ==

int resp, n1 = 10, n2 = 20;

n1 < n2 ? printf("Sim") :printf("Não");
n1 < n2 ? resp = 10 : resp = -10;
printf("%i", resp);
       
TELA: | SIM |
	  |  10 |

//Utilizado Para Quando Houver Somente Duas Coisas a Acontecer, Porém não Muito Usado.

===================================================================================================

===================================================================================================

	== Módulo(MOD) ==

if(variavel % 3 == 0){
	printf("É Divisivel por 3");
}
else if(variavel % 3 == 1){
	printf("Não É Divisivel por 3");
}

//Utilizado para Descobrir o Resto.

===================================================================================================

===================================================================================================

	== Estrutura ==

#include <stdio.h>

struct horario{
	
	int hora;
	int minuto;
	int segundo;
};

//Estrutura Criada Junto de Suas Variaveis.

int main(void){

	struct horario x;

	x.horas = 12;
	x.minuto = 55;
	x.segundo = 30;

	printf("%i: %i: %i\n", x.horas, x.minuto, x.segundo);
	return 0;
}

//Variavel "x" do Tipo "horario" Criada, Logo Após foi Dado Valores as Variaveis e Imprimidos.

===================================================================================================

===================================================================================================

	== Casting(CAST) ==

int num1 = 16;
int num2 = 3;
float resultado = (float) num1/num2;
printf("%f", resultado);

TELA: | 5.33 |

//Utilizado Para Mostrar o Real Valor de Uma Variavel.

===================================================================================================

===================================================================================================

	== Getchar ==

getchar();

//Utilizado Para Capturar o Ultimo Caractere Adicionado.

===================================================================================================

===================================================================================================

	== Strcpy ==

strcpy(variavel, "Texto");
strcpy(vetor[], "variavel");

//Utilizado para Inserir Texto em Variaveis ou Até Mesmo Receber um Certo Texto de Outra Variavel.
//OBS: Somente Variaveis Strings.

===================================================================================================

===================================================================================================

	== Malloc ==

struct estrutura
{
	char Nome[50];
	int codigo;
};

struct estrutura *novo;

novo = malloc(sizeof(struct estrutura));

//Utilizado Para Alocar um Espaço na Memória.

===================================================================================================

===================================================================================================

	== Sizeof ==

//Utilizado Para Dizer o Tamanho do Tipo do Dado que Está em Uso.

===================================================================================================

===================================================================================================

	== Typedef ==

typedef struct estruturaEndereco{
	
	char nome[50];

}Endereco; //Endereco Passa a Ser o Nome e estruturaEndereco seu "apelido".

===================================================================================================

===================================================================================================

	== Vetor ==

int vetor[5];
int tabela[5][5];
int matriz[5][5][5];

//Utilizado Para Receber Valores.

===================================================================================================

===================================================================================================
