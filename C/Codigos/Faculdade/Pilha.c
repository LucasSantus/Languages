#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct EstruturaPilha{
  int codigo;
  struct EstruturaPilha *anterior;
  struct EstruturaPilha *proximo;
} Pilha;

void Empilhar_Pilha(Pilha **inicio, Pilha **fim){
  Pilha *novo = malloc(sizeof(Pilha)); //usado para inserir valores na estrutura
  Pilha *aux = *inicio;
  
  printf("\n---------- Cadastro - Pilha -----------\n");
  printf("\nInforme o Código: ");
  scanf("%i", &novo->codigo);
  getchar();
  
  if(aux == NULL){
    novo->anterior = NULL;
    novo->proximo = NULL;
    *inicio = novo;
    *fim = novo;
  }
  else{
    novo->proximo = NULL;
    novo->anterior = *fim;
    (*fim)->proximo = novo;
    (*fim) = novo;
  }
}

void Listar_Pilha(Pilha *inicio, Pilha **fim){

  if(inicio == NULL){
    printf("Não Há Registros!\n");
  }
  else{
    printf("\n---------------------------------------");
    printf("\n------------ Imprimindo... ------------\n");

    Pilha *aux = *fim;
    printf("\n--------------- Topo... ---------------");
    while(aux != NULL){
      printf("\n--------- Imprimindo - Pilha ----------\n");
      printf("Código do Usuário: %i\n", aux->codigo);
      aux = aux->anterior;
    }
  }
  return;
}

void Desempilhar_Pilha(Pilha *aux, Pilha **inicio, Pilha **ultimo){

  if(inicio == NULL){
    printf("Não Há Registros!\n");
    return;
  }
  aux = *ultimo;
  
  if(aux->anterior == NULL){
    *inicio = NULL;
  }
  else{
    *ultimo = aux->anterior;
    (*ultimo)->proximo = NULL;
  }

  printf("Registro excluído: %i\n", aux->codigo);
  free(aux);
  return;
}

void Tamanho_Pilha(Pilha *inicio, Pilha **fim){
  Pilha *aux = *fim;
  int tamanho = 0;

  if(inicio == NULL){
    printf("Não Há Registros!\n");
  }
  else{
    while(aux != NULL){
      aux = aux->anterior;
      tamanho++;
    }
    printf("Tamanho da Pilha Atual: %i Dado(s)", tamanho);
  }
  return;
}

int main(void) {
  Pilha *p, *aux, *inicio = NULL;
  int opcao = 1;

  printf("|-----------------------------------------------|\n");
  printf("|------------------  MENU  ---------------------|\n");
  printf("|----------|  EMPILHAR   - NUMBER 1  |----------|\n");
  printf("|----------|   LISTAR    - NUMBER 2  |----------|\n");
  printf("|----------| DESEMPILHAR - NUMBER 3  |----------|\n");
  printf("|----------|   TAMANHO   - NUMBER 4  |----------|\n");
  printf("|----------|  DESTRUIR   - NUMBER 5  |----------|\n");
  printf("|----------|    SAIR     - NUMBER 0  |----------|\n");
  printf("|-----------------------------------------------|\n");

  while(opcao != 0){

    printf("\n------------------------------------------------\nSelecione a Opção:");
    scanf("%i", &opcao);

    switch(opcao){

    case 1:
      
      Empilhar_Pilha(&inicio, &p);
      break;

    case 2:
    
      Listar_Pilha(inicio, &p);
      break;

    case 3:

      Desempilhar_Pilha(inicio, &inicio, &p);
      break;

    case 4:

      Tamanho_Pilha(inicio, &p);
      break;

    case 5:
      aux = p;
      while(aux != NULL){
        Desempilhar_Pilha(inicio, &inicio, &p);
        aux = aux->anterior;
      }
      break;
      
    case 0:
      printf("Só Sucesso!");
      break;

    default:
      printf("Escolha Não Identificado!");
      break;
    }
  }
return 0;
}