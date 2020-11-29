/*
	//
*/

	------- LISTA DE ANOTAÇÕES - JAVA -------

	|---------------------------------------|
	|  OPERADOR | 	AÇÃO(Nome)				|
	|-----------|---------------------------|
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

public class main{
	public static void main(String[] args) {
		//Pacotes
		//Classes
		//Métodos
		//Variaveis
	}
}
//Estrutura Padrão.

===================================================================================================

===================================================================================================

	== Scanner ==

import java.util.Scanner;

Scanner in = new Scanner(System.in);
Tipo Variavel = in.nextTipo();

//Insere Valores as Variaveis.

===================================================================================================

===================================================================================================

	== Println ==

System.out.Println("Texto" + variavel + "Texto");

//Bastante Usado para Imprimir na Tela.

===================================================================================================

===================================================================================================

	== Printf ==

printf("Mensagem"); 

//Bastante Usado para Imprimir na Tela.

===================================================================================================

===================================================================================================

	== Tipo Inteiro ==

int variavel = 10;
Scanner in = new Scanner(System.in);
int variavel = in.nextInt(); 	//Valores Recebidos...
println("Texto" + variavel);

//Números com Valores Inteiros.

===================================================================================================

===================================================================================================

	== Tipo Float ==

float variavel = 10.59;
Scanner in = new Scanner(System.in);
float variavel = in.nextFloat();	//Valores Recebidos...
println("Texto" + variavel);

//Números com Ponto, Pequenos.

===================================================================================================

===================================================================================================

	== Tipo Char ==

char variavel = "Letras";
Scanner in = new Scanner(System.in);
char variavel = in.nextChar();	//Valores Recebidos...
println("Texto" + variavel);

//Adiciona Letras em uma Variavel, Caso Deseje Adicionar Textos, Seria Recomendado usar Strings.

===================================================================================================

===================================================================================================

	== Tipo String ==

import java.lang.String;

String variavel = "Texto";
String [] variavel = new String[5];
Scanner in = new Scanner(System.in);
String variavel = in.nextString();
println("%s", variavel);

//Possibilita Adicionar Textos a uma Variavel.

===================================================================================================

===================================================================================================

	== Tipo Double ==

double variavel = 17.68456975;
Scanner in = new Scanner(System.in);
Double variavel = in.nextDouble();
println("Texto" + variavel);

//Números com Ponto, Grandes.

===================================================================================================

===================================================================================================

	== Tipo Byte ==

double variavel = 93;
Scanner in = new Scanner(System.in);
byte variavel = in.nextByte();
println("Texto" + variavel);

//Utiliza Valores de -128 á 127. 

===================================================================================================

===================================================================================================

	== Tipo Short ==

double variavel = 211895496548;
Scanner in = new Scanner(System.in);
Double variavel = in.nextDouble();
println("Texto" + variavel);

//Utiliza Valores de -2.147.483.648 á 2.147.483.647.

===================================================================================================

===================================================================================================

	== Tipo Long ==

long int variavel = 176845696724575;
long double variavel = 17.64325468456975;
Scanner in = new Scanner(System.in);
Tipo variavel = in.nextTipo();
println("Texto" + variavel);

//Possibilita Adicionar Números Maiores as Variaveis.

===================================================================================================

===================================================================================================

	== Tipo Bool ==

boolean variavel = true or false;
println(variavel);

//Utilizado para Variaveis Binárias(Booleandas)(True or False).

===================================================================================================

===================================================================================================

	== Constantes ==

final int variavel = 17;				
final float variavel = 1.27;			
final double variavel = 11.876514278;	

//Possibilita o Valor da Variavel a Nunca Mudar Durante a Execução.

===================================================================================================

===================================================================================================

	== Estrutura de Repetição "For" ==

for (int i = 0; i < TamanhoMaximo; i++){
	//code
}

//Bastante Usado Para Repetições.

===================================================================================================

===================================================================================================

	== Estrutura de Repetição "While" ==

variavel = 1

while(variavel != 0){
	//code
	//executará!!
}

//Executará o Loop Somente se for Verdadeira.

===================================================================================================

===================================================================================================

	== Estrutura de Repetição " Do While" ==

variavel = 1

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

	== Break ==

break;

//Utilizado Para Quebrar, Finalizar algo, Bastante Usada para romper um looping.


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

variavel = (n1 < n2) ? printf("Sim") :printf("Não");
variavel = (n1 < n2) ? resp = 10 : resp = -10;
println("%i", resp);
       
TELA: | SIM |
	  |  10 |

//Utilizado Para Quando Houver Somente Duas Coisas a Acontecer, Porém não Muito Utilizado.

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

	== Random ==

import java.util.Random;

Random variavel = new Random();
System.out.Println(variavel.nextTipo(limite));

//Utilizada para Criar Números Aleatórios.

===================================================================================================

===================================================================================================

	== Label ==

labelForI: for (int a = 0; a < TamanhoMaximo; ++a){
				for (int b = 0; b< TamanhoMaximo; ++b){
					for (int c = 0; c < TamanhoMaximo; ++c){
						break labelForI;
					}
				}
			}
//Quando Está se Referindo a Algo.			

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

	== Blocos de Instrução ==

Nome1:{
	//code
	Nome2:{
		//code
		Nome3:{
			//code
			break Nome1;
		}
	}
}

===================================================================================================

===================================================================================================

	== Continue ==

for (int i = 0; i < variavel; ++i){
	if (true) {
		continue;
	}
}
//Utilizado para Encerrar um Ciclo, Mais Continua o Loop.


===================================================================================================

===================================================================================================

	== Length ==

for (int i = 0; i < array.Length; ++i){
	//code
}	

//Utilizado Para Dizer o Tamanho do Tipo do Dado que Está em Uso.

===================================================================================================

===================================================================================================

	== For - Each ==


int [] array = new int[3];
	array[0] = 10;
	array[1] = 20;
	array[2] = 30;
	for(int variavel:array){
		variavel;
	}

===================================================================================================

===================================================================================================

	== Array ==

int [] vetor = new int[3];
int [][] tabela = new int[3][3];
int [][][] matriz = new int[3][3][3];

//Utilizado Para Receber Valores.

===================================================================================================

===================================================================================================

	------- LISTA DE ANOTAÇÕES - JAVA ORIENTADO A OBJETOS -------

	== Inicio ==

class Nome{}

---------------------------------------------

class nome Extends nome{}

---------------------------------------------

class nome Extends nome Implements nome{}

---------------------------------------------

public class main{
	public static void main(String[] args) {
		//Classe Principal.
		//Função/Método Principal.
		//Somente uma Classe Pública.
	}
}

===================================================================================================

===================================================================================================

1. Modificadores de Acesso;
A. public
B. private
C. protected
D. sem modificadores

2. Atribuir um Nome a Classe;
3. Extender de Outra Classe ("Extends");
4. Interface que Implementa uma Classe("Implements");
5. O Corpo da Classe.

===================================================================================================

===================================================================================================

	== Classe ==

[Modificador][Tipo]Nome{}

public class main{}

===================================================================================================

===================================================================================================

	== Função/Método ==

public static void main(String[] args) {
	Metodo();
}

===================================================================================================

===================================================================================================

	== Estrutura ==

class Estrutura{

	public boolean ligado;
	private boolean displayOn;
	public int volume = 0;

}

public class main{
	public static void main(String [] args){
		Estrutura struct;
		struct = new Estrutura();
		struct.volume = 5;
		struct.ligado = true;
		struct.displayOn = false;
	}
}

===================================================================================================

===================================================================================================

	== Parâmetro ==

[Tipo][Nome](Parâmetro){}

class calculo{ //Classe Para Criar o Parâmetro
	Void Soma(int num1, int num2){ //Parâmetro
		System.out.Println(num1+num2);
	}
}

public class main{	//Classe Principal
	public static void main(String[] args) { //Função/Método Principal
		calculo total = new calculo(); //Variavel do Tipo "calculo" Criada.
		total.Soma(5,35); //Variavel "total" Chamando o Método "soma", Logo Após, Trocando Informações.
	}
}

===================================================================================================

===================================================================================================

	== Retornando Valores ==

public int num1, num2;

class retornar{ 
	Void Multiplicação(int num1, int num2){ 
		return num1 * num2;
	}
}

public class main{	//Classe Principal
	public static void main(String[] args) { 
		retornar total = new retornar(); 
		total.Multiplicação(5,35); 
	}
}

===================================================================================================

===================================================================================================

	== Overloading "Sobrecarga de Métodos" ==

//Um Bom Exemplo da Sobrecarga de Métodos, Se Não For Um, Pode Ser Outro, Mais ou Menos igual ao "IF/Else If/ Else".

class Carga{
	void imprime(String S){
		System.out.Println(S);
	}
	void imprime(String S1, String S2){
		System.out.Println(S1 + "-" + S2);
	}
	void imprime(String S, String I){
		System.out.Println(S + "-" + I);
	}
}

public class main{
	public static void main(String[] args) {
		New Carga().imprime("Texto");
		New Carga().imprime("Texto", "Texto");
		New Carga().imprime("Texto", 25);
	}
}

===================================================================================================

===================================================================================================

	== Recursividade ==

//Recursividade, Chama a si Mesmo, Propondo Menas Linhas de Códigos, Porém Gasta Mais Processamento.

class Fatorial{
	int fat(int Num){
		if(Num <= 1){
			return 1;
		}
		return fat(Num-1)*Num; //Retorna o Fatorial.
	}
}

===================================================================================================

===================================================================================================

	== Construtores ==

class Janela{
	int largura, altura;
	Janela(int l, int a){ //Contrutor
		largura = l;
		altura = a;
	}
	void imprime(){
		System.out.Println(l + "-" + a);
	}
}

public class main{
	public static void main(String[] args) {
		Janela j = new Janela(250,300);
		j.imprime();
	}
}

//O Construtor Tem Sempre o Mesmo Nome da Classe.

===================================================================================================

===================================================================================================

	== This ==

class Janela{
	int largura, altura;
	Janela(int largura, int altura){
		this.largura = largura;
		this.altura = altura;
	}
}

//Faz Com Que as Variaveis se Referem a Membros de Classe.

===================================================================================================

===================================================================================================
