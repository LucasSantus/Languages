/*
	//
*/

	------- LISTA DE ANOTAÇÕES - DART -------

	|---------------------------------------|
	|  OPERADOR | 	AÇÃO(Nome)				|
	|-----------|---------------------------|
	|	& 		|	And                     |
	|	| 		|	Or 						|
	|	--		|	Declemento				|
	|	++ 		|	Inclemento				|
	|	- 		|	Subtração				|
	|	+ 		|	Adição					|
	|	% 		|	Módulo (MOD)			|
	|	* 		|	Multiplicação			|
	|	/ 		|	Divisão					|
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

void main(){

		//Pacotes
		//Classes
		//Métodos
		//Variaveis

}
//Estrutura Padrão.

===================================================================================================

===================================================================================================

	== Print ==

print("Mensagem"); 

//Bastante Usado para Imprimir na Tela.

===================================================================================================

===================================================================================================

	== Tipo Var ==

var variavel = 10; 
print("Texto ${variavel} ou $variavel ou" + variavel);

//Variavel sem tipo, o tipo pode ser mudado de acordo com as necessidades.
===================================================================================================

===================================================================================================

	== Tipo Inteiro ==

int variavel = 10;
print("Texto ${variavel} ou $variavel ou" + variavel);

//Números com Valores Inteiros.

===================================================================================================

===================================================================================================

	== Tipo Dynamic ==

dynamic teste = 1;
print("Texto ${variavel} ou $variavel ou" + variavel);

//Descobre por si mesmo, qual o tipo da variavel.

===================================================================================================

===================================================================================================

	== Tipo String ==

String variavel = "Texto";
print("Texto ${variavel} ou $variavel ou" + variavel);

//Possibilita Adicionar Textos a uma Variavel.

===================================================================================================

===================================================================================================

	== Tipo Double ==

double variavel = 17.68456975;
print("Texto ${variavel} ou $variavel ou" + variavel);

//Números com Ponto, Grandes.

===================================================================================================

===================================================================================================

	== Tipo Bool ==

bool variavel = true or false;
print("Texto ${variavel} ou $variavel ou" + variavel);

//Utilizado para Variaveis Binárias(Booleandas)(True or False).

===================================================================================================

===================================================================================================

	== Constante ==

const int variavel = 17;							
const double variavel = 11.876514278;	
const String variavel = "Text"

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

	== Random ==

import 'dart:math' show Random;

void main() {
  var randomizer = new Random(); //Instanciando o Random.

  var num = randomizer.nextInt(100); //O Limite pode ser alterado como desejar.
  print(num);
  
}

//Utilizada para Criar Números Aleatórios.

===================================================================================================

===================================================================================================

	== Casting(CAST) ==

	?????

//Utilizado Para Mostrar o Real Valor de Uma Variavel.

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

	------- LISTA DE ANOTAÇÕES - DART ORIENTADO A OBJETOS -------

	== Inicio ==

class Nome{}

---------------------------------------------

class nome Extends nome{}

---------------------------------------------

class nome Extends nome Implements nome{}

---------------------------------------------

void main(){

		//Função/Método Principal.
		//Somente uma Classe Pública.
}

===================================================================================================

===================================================================================================

	== Classe ==

[Modificador][Tipo]Nome{}

class main{
	
}

===================================================================================================

===================================================================================================

	== Função/Método ==

void main(){
	Metodo();
}

===================================================================================================

===================================================================================================

	== Classes e Objetos ==

class Casa { 									//Classe
  String cor; 									//Atributos
  
  void abrirJanela(){ 							//Métodos
    print("Abrir janela da casa $cor ");
  }
  void abrirPorta(){
    print("Abrir porta da casa $cor ");
  }
  void abrirCasa(){
    this.abrirJanela();
    this.abrirPorta();
  }
}

class Usuario {
  
  String usuario;
  String senha;
  
  void autenticar(){
    
    var usuario = "jamilton@gmail.com";			//Recuperar de um banco de dados
    var senha = "123456";						//Recuperar de um banco de dados
    
    if( this.usuario == usuario && this.senha == senha ){ 			//this, refere-se a atributo dessa classe.
      print("Usuário autenticado");
    }else{
      print("Usuário não autenticado");
    }
  }
}

void main() {
  
  Usuario usuario = Usuario();
  
  usuario.usuario = "jamilton@gmail.com";		 //Digitados pelo usuario do seu App
  usuario.senha = "12345";						 //Digitados pelo usuario do seu App
  
  usuario.autenticar();
  
  Casa minhaCasa = Casa();
  minhaCasa.cor = "Amarela";
  minhaCasa.abrirJanela();
  minhaCasa.abrirPorta();
  minhaCasa.abrirCasa();
}

===================================================================================================

===================================================================================================

	== Estrutura ==

class Estrutura{

	public boolean ligado;
	private boolean displayOn;
	public int volume = 0;

}

void main(){
		Estrutura struct;
		struct = new Estrutura();
		struct.volume = 5;
		struct.ligado = true;
		struct.displayOn = false;
}

===================================================================================================

===================================================================================================

	== Parâmetro ==

[Tipo][Nome](Parâmetro){}

class calculo{ //Classe Para Criar o Parâmetro
	void Soma(int num1, int num2){ //Parâmetro
		print(num1+num2);
	}
}

void main(){	//Função Principal
	calculo total = new calculo(); //Variavel do Tipo "calculo" Criada.
	total.Soma(5,35); //Variavel "total" Chamando o Método "soma", Logo Após, Trocando Informações.
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

void main(){
		retornar total = new retornar(); 
		total.Multiplicação(5,35); 
}

===================================================================================================

===================================================================================================


			???


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

void main(){
		New Carga().imprime("Texto");
		New Carga().imprime("Texto", "Texto");
		New Carga().imprime("Texto", 25);
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
		print(l + "-" + a);
	}
}

void main(){
		Janela j = Janela(250,300);
		j.imprime();
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

	== Funções ==

void exibirMensagem(String nome, int idade){
  print("Olá $nome !");
  print("Idade: $idade ");
}
 
void main() {
  exibirMensagem("Lucas", 19);
  exibirMensagem("Eduardo", 21);
}

===================================================================================================

===================================================================================================

	== Funcões Anônimas ==

void exibirDados(String nome, int idade, {double altura}){ //altura é opcional
  var novaAltura = altura ?? 0; //Caso Altura for NULL, não recebeu valor, irá receber 0
  print("nome: $nome");
  print("idade: $idade");
  print("altura: $novaAltura");
}

void calcularBonus(){
  print("seu bônus é de: 20");
}

void calcularSalario(double salario, Function funcaoParametro){
  print("Seu salário é: $salario ");
  funcaoParametro();
}

void main() {
  exibirDados("Lucas", 19, altura: 1.77);
  calcularSalario(100, (){
    print("Calculo customizado");
  } );

}

===================================================================================================

===================================================================================================

	== Vetor ==

void main() {
  
  var nomes = [
    "Lucas", 
    "Eduardo", 
    "Santos"
  ];
  
  var numeros = [
    100, 
    200, 
    300
  ];
  
  print( numeros );
  print( nomes );
  
}

===================================================================================================

===================================================================================================

	== Getter e Setter ==

class Conta {
  
  double saldo = 0;
  double _saque = 0;
  
  double get saque { //Getter -> Obter
    //Validacoes

    return this._saque;
  }

  set saque(double saque){  //Setter -> Configurar
    if( saque > 0 && saque <= 500 ){
      this._saque = saque;
    }
  }
}

void main() {
  Conta conta = Conta();
  conta.saque = 900;

  print( conta.saque );
}

===================================================================================================

===================================================================================================

	== Herança ==

class Animal {
  String cor;
  void dormir(){
    print("Dormir");
  } 
}

class Cao extends Animal { 
  String corOrelha;
  void latir(){
    print("Latir");
  }
}

class Passaro extends Animal {
  String corBico;
  void voar(){
    print("Voar");
  }
}

void main() {
  
  Cao cao = Cao();
  Passaro passaro = Passaro();
  
  cao.cor = "Branco";
  cao.corOrelha = "Preto";
  print( "Cor do cão: " + cao.cor );
  print( "Cor da orelha: " + cao.corOrelha );
  cao.latir();
  
  passaro.cor = "Marrom";
  print( passaro.cor );
  passaro.voar();

}

===================================================================================================

===================================================================================================

	== Sobrescrita de Métodos ==

class Animal {
  String cor;
  Animal(this.cor);
  void dormir(){
    print("Dormir");
  } 
  
  void correr(){
    print("Correr ");
    print("como");
    print("um");
  }
}

class Cao extends Animal { 
  String corOrelha;
  Cao(String cor, this.corOrelha) : super(cor);
  void latir(){
    print("Latir");
  }
  
  @override //sobrepor
  void correr(){
    super.correr();
    print(" cão!");
  }
}

class Passaro extends Animal {
  String corBico;
  Passaro(String cor, this.corBico) : super(cor);
  void voar(){
    print("Voar");
  }
  
  @override //sobrepor
  void correr(){
    super.correr();
    print(" passaro!");
  }
}

void main() {
  
  Cao cao = Cao("Marrom", "Branco");
  Passaro passaro = Passaro("Vermelho", "Amarelo");
  print( "Passaro cor: ${passaro.cor} corBico: ${passaro.corBico} " );
  
  /*
  cao.correr();
 	passaro.correr(); 
 
  cao.cor = "Branco";
  cao.corOrelha = "Preto";
  print( "Cor do cão: " + cao.cor );
  print( "Cor da orelha: " + cao.corOrelha );
  cao.latir();
  
  passaro.cor = "Marrom";
  print( passaro.cor );
  passaro.voar();
  */
}

===================================================================================================

===================================================================================================

	== Modificadores Static e Final ==

class Configuracoes {
  
  static String identificadorApp = "ADF5454SDFAGH";
  static String notificacaoSom = "sim";
  
  static void configuracaoInicial(){
    print( "Executa configuracoes iniciais" );
  }
}

class Conta {
  String valor;
}

void main() {
  
  //Modificadores Static e Final
  //Configuracoes config = Configuracoes();
  //Configuracoes.configuracaoInicial();
  //print( Configuracoes.notificacaoSom );
  
  final Conta conta = Conta();
  conta.valor = "Jamilton";
  
  conta = Conta();
  print( conta.valor );
}

===================================================================================================

===================================================================================================

	== Interface ==
/*
*	Pode-se dizer, a grosso modo, que uma 	interface é um contrato que quando assumido por uma classe deve ser 
*	implementado
*
*	Interface é utilizada pois podemos ter muitos objetos (classes) que podem possuir a mesma ação (métodos), porém, 
*	podem executá-las de maneiras diferentes
*/

abstract class Presidenciavel {
  void participarEleicao();
}

abstract class Jornalismo {
  void escreverArtigoJornal();
}

abstract class Cidadao {
  void direitosDeveres(){
    print("Todo cidadão tem direitos e deveres");
  }
}

class Obama extends Cidadao 
  implements Presidenciavel, Jornalismo  {
  
  @override
  void escreverArtigoJornal(){
    print("Escrever artigo Jornal");
  }
  
  @override
  void participarEleicao(){
    print("Eleição nos Estados Unidos para o Obama");
  }   
}

class Jamilton extends Cidadao {
  
}

void main() {
	
  Obama obama = Obama();
  obama.direitosDeveres();
  obama.participarEleicao();
  
  Jamilton jamilton = Jamilton();
  jamilton.direitosDeveres();
}

===================================================================================================

===================================================================================================

	== Mixins ==

/* 
Mixins é uma maneira de utilizar códigos em múltiplas hierarquias de classes
*/

abstract class Presidenciavel {
  void participarEleicao();
}

abstract class Jornalismo {
  void escreverArtigoJornal();
}

mixin Escrita {
  
  void escreverArtigoJornal(){
    print("Escrever um artigo para o Jornal");
  }
}

abstract class Cidadao {
  void direitosDeveres(){
    print("Todo cidadão tem direitos e deveres");
  }
}

class Obama extends Cidadao 
  implements Presidenciavel, Jornalismo  {
  
  @override
  void escreverArtigoJornal(){
    print("Escrever artigo Jornal");
  }
  
  @override
  void participarEleicao(){
    print("Eleição nos Estados Unidos para o Obama");
  } 
}

class Jamilton extends Cidadao with Escrita {
  
}

void main() {
	
  Obama obama = Obama();
  obama.direitosDeveres();
  obama.participarEleicao();
  
  Jamilton jamilton = Jamilton();
  jamilton.direitosDeveres();
  jamilton.escreverArtigoJornal();
}

===================================================================================================

===================================================================================================

	== Coleções - Listas ==

/*
Collection ou coleções -> são implementações de estruturas de dados, que é utilizado para armazenar itens
 - List
 - Maps
*/

class Usuario {
  
  String nome;
  int idade;
  
  Usuario(this.nome, this.idade);
}

void main() {

  List<String> frutas = ["Morango", "Manga", "Melancia"];
  //List numero = [1, 5, "Jamilton", 10.60];
  
  //adicionar itens
  //frutas.add("Melancia");
  //Inserir em uma posição
  //frutas.insert(1, "Abacaxi");
  
  //Remover item
  //frutas.removeAt(1);
  
  //Verificar item na lista
  //print( frutas.contains("Pera") );
  
  //tamanho da lista
  //print( frutas.length );
  //print( frutas );
  
  //Armazenar objetos
	
  List<Usuario> usuarios = List();
  usuarios.add( Usuario("Jamilton", 30) );
  usuarios.add( Usuario("Leticia", 28) );
  usuarios.add( Usuario("Jorge", 30) );
  
  for( Usuario usuario in usuarios ){
    print( "Nome: ${usuario.nome} idade: ${usuario.idade}" );
  }
  //print( usuarios );  
}

===================================================================================================

===================================================================================================

	== Coleções - Mapas == 

/*
Collection ou coleções -> são implementações de estruturas de dados, que é utilizado para armazenar itens
 - List
 - Maps
*/

void main() {
	
  /*
  chave -> valor
  List frutas = ["Morango", "Manga"];
  print( frutas[0] );
  
  
  Map frutas = Map();
  frutas[0] = "Morango";
  frutas[1] = "Manga";
  print( frutas[0] );
  */
  
  //chave -> valor
  Map<String, String> estados = Map();
  estados["SP"] = "São Paulo";
  estados["MG"] = "Minas Gerais";
  estados["RJ"] = "Rio Janeiro";
  
  Map<String, dynamic> usuarios = Map();
  usuarios["nome"] = "Jamilton";
  usuarios["idade"] = 30;
  
  //print( estados.keys );
  //print( estados.values );
  //print( estados.containsKey("MA") );
  //print( estados.containsValue("Ceará") );
  //print( estados.length );
  /*
  estados.forEach(
  	(chave, valor) => print(" $chave - $valor ")
  );*/
  
  //print( estados );
  
}

===================================================================================================

===================================================================================================
