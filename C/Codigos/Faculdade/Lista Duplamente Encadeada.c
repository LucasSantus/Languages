#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct EstruturaAnimal{
  int codigo;
  char nome[50], especie[50],grupo[50];
  struct EstruturaAnimal *anterior;
  struct EstruturaAnimal *proximo;
} Animal;

void Cadastrar_Animal(Animal **inicio, Animal **fim){
  Animal *novo = malloc(sizeof(Animal));
  Animal *aux = *inicio;
  
  printf("\n--------- Cadastro - Animal ----------\n");
  printf("\nInforme o Código: ");
  scanf("%i", &novo->codigo);
  getchar();
  printf("Informe o Nome: ");
  fgets(novo->nome,50,stdin);
  printf("Informe a Espécie: ");
  fgets(novo->especie,50,stdin);
  printf("Informe o Grupo: ");
  fgets(novo->grupo,50,stdin);
 

  if(aux == NULL){
    novo->anterior = NULL;
    novo->proximo = NULL;
    *inicio = novo;
    *fim = novo;
  }
  else{

  while(aux != NULL && (novo->codigo > aux->codigo)){
    aux = aux->proximo;
  }

    //Ultimo da lista
    if(aux == NULL){
      novo->proximo = NULL;
      novo->anterior = *fim;
      (*fim)->proximo = novo;
      (*fim) = novo;
    }

    //Primeiro da lista
    else if(aux->anterior == NULL){
      novo->anterior = NULL;
      novo->proximo = *inicio;
      (*inicio)->anterior = novo;
      (*inicio) = novo;
    }

    //Meio da lista
    else{
      novo->proximo = aux;
      novo->anterior = aux->anterior;
      aux->anterior->proximo = novo;
      aux->anterior = novo;
    }
  }
}

void Listar(Animal **inicio, Animal **fim){
  if(inicio == NULL){
      printf("Não Há Registros!\n");
    }
    else{
      printf("\n---------------------------------------");
      printf("\n------------ Imprimindo... ------------\n");

      Animal *aux = *inicio;

      while(aux != NULL){
        printf("\n-------- Imprimindo - Animal ---------\n");

        printf("\nCódigo do Animal: %i", aux->codigo);
        printf("\nNome do Animal: %s", aux->nome);
        printf("Espécie do Animal: %s", aux->especie);
        printf("Grupo do Animal: %s", aux->grupo);
        
        aux = aux->proximo;
      }
      printf("\n");
    }

  return;
}

void Atualizar(Animal *aux){

  int pesquisa;

  printf("\n------------  Alterando... ------------\n");
  printf("Insira o Código a Ser Alterado:\n");
  scanf("%i",&pesquisa);
  getchar();

  while(aux != NULL){
    if(aux->codigo == pesquisa){

      printf("Informe o Novo Nome:\n");
      fgets(aux->nome, 50, stdin);
      printf("Informe a Nova Espécie:\n");
      fgets(aux->especie, 50, stdin);
      printf("Informe o Novo Grupo:\n");
      fgets(aux->grupo, 50, stdin);
      return;
    }
  aux = aux->proximo;
  }
  printf("Código Não Encontrado!\n");

}

void Deletar(Animal *aux, Animal **inicio, Animal **ultimo){

  //Checa se lista está vazia
  if(aux == NULL){
    printf("Lista Vazia!\n\n");
    return;
  }

  int pesquisa;

  printf("Insira o Código a ser Deletado: ");
  scanf("%i",&pesquisa);
  getchar();

  while(aux != NULL){
    if(aux->codigo == pesquisa){
      if(aux->anterior == NULL){
        *inicio = aux->proximo;
      }
      else{
        aux->anterior->proximo = aux->proximo;
      }
      if(aux->proximo == NULL){
        *ultimo = aux->anterior;
      }
      else{
        aux->proximo->anterior = aux->anterior;
      }
      printf("Registro excluído: %i\n %s\n %s\n %s\n ", aux->codigo, aux->nome, aux->especie,aux->grupo);
      free(aux);
      return;
    }
    aux = aux->proximo;
  }
  printf("Código não encontrado\n\n");
  return;
}

int main(void) {
Animal *p, *aux, *inicio = NULL;
int opcao=1;

  printf("\n|------------------  MENU  ------------------|\n");
  printf("|-------  CADASTRAR ANIMAL - NUMBER 1  ------|\n");
  printf("|----------   LISTAR   - NUMBER 2  ----------|\n");
  printf("|----------   ALTERAR  - NUMBER 3  ----------|\n");
  printf("|----------   DELETAR  - NUMBER 4  ----------|\n");
  printf("|----------    SAIR    - NUMBER 0  ----------|\n");
  printf("|--------------------------------------------|\n\n\n");

  while(opcao != 0){
  printf("\n---------------------------------------\nSelecione a Opção:");
  scanf("%i",&opcao);

    switch(opcao){
      case 1:
        Cadastrar_Animal(&inicio,&p);
        break;

      case 2:
        Listar(&inicio,&p);
        break;

      case 3:
        Atualizar(inicio);
        break;

      case 4:
        Deletar(inicio, &inicio, &p);
        break;
      
      case 0:
        printf("ARIGATO!");
        break;
      default:
        printf("Opção Inválida!");
        break;
    }
  }
  return 0;
}
