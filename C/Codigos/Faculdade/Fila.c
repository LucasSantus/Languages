#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct EstruturaFila{
  int codigo;
  struct EstruturaFila *anterior;
  struct EstruturaFila *proximo;
} Fila;

void Enfileirar_Fila(Fila **inicio, Fila **fim){
  Fila *novo = malloc(sizeof(Fila)); //usado para inserir valores na estrutura
  Fila *aux = *inicio;
  
  printf("\n--------- Cadastro - Fila ----------\n");
  printf("\nInforme o Código: ");
  scanf("%i", &novo->codigo);
  getchar();

  //Se não tiver códigos
  if(aux == NULL){
    novo->anterior = NULL;
    novo->proximo = NULL;
    *inicio = novo;
    *fim = novo;
  }
  //Joga o registro no final  
  else{
    novo->proximo = NULL;
    novo->anterior = *fim;
    (*fim)->proximo = novo;
    (*fim) = novo;
  }
}

void Listar_Fila(Fila *inicio){
  if(inicio == NULL){
    printf("Não Há Registros!\n");
  }
  else{
    printf("\n--------------------------------------------------");
    printf("\n------------ Imprimindo... ------------\n");

    Fila *aux = inicio;

    printf("\n-------------   Fim...  ---------------\n");
    
    while(aux != NULL){
      
      printf("\n---------  Imprimindo - Fila ----------\n");
      printf("Código do Usuário: %i\n", aux->codigo);
  
      aux = aux->proximo;
    }
  }
  return;
}

void Desenfileirar_Fila(Fila *aux, Fila **inicio, Fila **ultimo){

  if(aux == NULL){
    printf("Não Há Registros!\n");
  return;
  }

  aux = *inicio;

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
      
  printf("Registro excluído: %i\n", aux->codigo);
  free(aux);
  return;
}

void Tamanho_Fila(Fila *inicio){
  Fila *aux = inicio;
  int tamanho = 0;
  if(inicio == NULL){
    printf("Não Há Registros!\n");
  }
  else{
    while(aux != NULL){
      aux = aux->proximo;
      tamanho++;
    }
    printf("Tamanho da Fila Atual: %i Dado(s)", tamanho);
  }
  return;
}

int main(void) {
  Fila *p, *aux, *inicio = NULL, *fim;
  int opcao = 1;

  printf("\n|------------------  MENU  -----------------------|\n");
  printf("|----------   ENFILEIRAR    - NUMBER 1  ----------|\n");
  printf("|----------    LISTAR       - NUMBER 2  ----------|\n");
  printf("|----------  DESENFILEIRAR  - NUMBER 4  ----------|\n");
  printf("|----------    TAMANHO      - NUMBER 5  ----------|\n");
  printf("|----------     SAIR        - NUMBER 0  ----------|\n");
  printf("|-------------------------------------------------|\n");

  while(opcao != 0){

    printf("\n--------------------------------------------------\nSelecione a Opção:");
    scanf("%i", &opcao);

    switch(opcao){

    case 1:
      Enfileirar_Fila(&inicio, &p);
      break;

    case 2:
      Listar_Fila(inicio);
      break;

    case 3:
      Desenfileirar_Fila(inicio, &inicio, &p);
      break;

    case 4:
      Tamanho_Fila(inicio);
      break;

    case 5:
      aux = inicio;
      while(aux != NULL){
        Desenfileirar_Fila(inicio, &inicio, &p);
        aux = aux->proximo;
      }
      break;
      
    case 0:
      printf("Só Sucesso!");
      break;

    default:
      printf("Código Não Identificado!");
      break;
    }
  }
return 0;
}