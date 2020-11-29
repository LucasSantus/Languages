//Algoritmo complexo do SJF.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define quantum 5
int qntd = 0;

typedef struct EstruturaProcesso{
  char nome[50];
  int tipo, bloqueio, conf, tmpExecucao;
  struct EstruturaProcesso *anterior;
  struct EstruturaProcesso *proximo;
} Processo;

void Adicionar_Processo(Processo **inicio, Processo **fim){
  Processo *job = malloc(sizeof(Processo));
  Processo *aux = *inicio;

  printf("\n--------- Adicionar - jobs ----------\n");
  printf("\n--- Processos Para Escalonar (Entre 1 e 100)---\n");
  getchar();

  printf("Informe o Nome: ");
  fgets(job->nome,50,stdin);

  printf("Tempo de Execução: ");
  scanf("%i", &job->tmpExecucao);

  printf("--  CPU | 1  -- \n--  E/S | 2  --");
  printf("\nInforme o Tipo: ");
  scanf("%i", &job->tipo);
  qntd++;

  if(aux == NULL){
    job->anterior = NULL;
    job->proximo = NULL;
    *inicio = job;
    *fim = job;
  }
  else{
    while(aux != NULL && (job->tmpExecucao > aux->tmpExecucao)){
      aux = aux->proximo;
    }

    //Ultimo da lista
    if(aux == NULL){
      job->proximo = NULL;
      job->anterior = *fim;
      (*fim)->proximo = job;
      (*fim) = job;
    }

    //Primeiro da lista
    else if(aux->anterior == NULL){
      job->anterior = NULL;
      job->proximo = *inicio;
      (*inicio)->anterior = job;
      (*inicio) = job;
    }

    //Meio da lista
    else{
      job->proximo = aux;
      job->anterior = aux->anterior;
      aux->anterior->proximo = job;
      aux->anterior = job;
    }
  }
}

void Listar_Processo(Processo *inicio){
    
  if(inicio == NULL){
    printf("Não Há Processos!\n");
  }
  else{
    printf("\n--------------------------------------------------");

    Processo *aux = inicio;
    
    while(aux != NULL){
      if(aux->tmpExecucao >= 0){
        char conv[10];
        if(aux->tipo == 1){
          strcpy(conv, "CPU");
        }
        else if(aux->tipo == 2){
          strcpy(conv, "E/S");
        }
        printf("\n---------  Imprimindo - Processo  ----------\n");
        printf(" Temp Execução: %i | Tipo: %s |  Nome: %s", aux->tmpExecucao, conv, aux->nome);
        aux = aux->proximo;
      }
      else{ 
        if(aux->tipo == 1){
          printf("\nNão Há Processos CPU's Bounds\n");
          break;
        }
        if(aux->tipo == 2){
          printf("\nNão Há Processos E/S\n");
          break;
        }
      }
    }
    aux = inicio;
    while(aux != NULL){
      if(aux->tipo == 2 && aux->bloqueio > 0){
        printf("\n---------  Processos Bloqueados  ----------\n");
        printf(" Bloqueio: %i | Nome: %s ", aux->bloqueio, aux->nome);
      }
      aux = aux->proximo;
    }
  }
  return;
}

void Executar_Processo(Processo *aux, Processo **inicio, Processo **ultimo){
  aux = *inicio;

  if(aux == NULL){
    printf("Não Há Processos!\n");
  return;
  }
  else{ 
    while(aux != NULL){
      if(aux->tmpExecucao <= 0){
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
        free(aux);
        qntd--;
      }
      else{
        if(aux->tipo == 1){
          aux->tmpExecucao -= quantum;
        }
        else{
          if(aux->bloqueio == 0){
            aux->tmpExecucao -= 1;
            aux->bloqueio = 2; //Tempo de uma operação de E/S
          }
          else{
            aux->bloqueio -= qntd;
          }
        } 
      }
      aux = aux->proximo;
    } 
  }
  return;
}

int main(void) {
  Processo *p, *aux, *inicio = NULL, *fim;
  int opcao = 1;

  printf("\n|--------------  MENU  --------------------------|\n");
  printf("|----------    ADICIONAR    - NUMBER 1  ---------|\n");
  printf("|----------     LISTAR      - NUMBER 2  ---------|\n");
  printf("|----------    EXECUTAR     - NUMBER 3  ---------|\n");
  printf("|----------     SAIR        - NUMBER 0  ---------|\n");
  printf("|------------------------------------------------|\n");

  while(opcao != 0){

    printf("\n--------------------------------------------------\nSelecione a Opção:");
    scanf("%i", &opcao);

    switch(opcao){

    case 1:
      Adicionar_Processo(&inicio, &p);
      break;

    case 2:
      Listar_Processo(inicio);
      break;

    case 3:
      Executar_Processo(inicio,&inicio, &p); 
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