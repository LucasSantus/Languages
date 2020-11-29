#include <stdlib.h>
#include <stdio.h>

typedef struct EstruturaNo{
  int valor;
  struct EstruturaNo *esquerda;
  struct EstruturaNo *direita;
} No;

void insereNo(No **raiz, int valor){

  No *novoNo = malloc(sizeof(No));
  novoNo->valor = valor;
  novoNo->esquerda = NULL;
  novoNo->direita = NULL;

  printf("Acessou a Raiz\n");

  if(*raiz == NULL){
    printf("Valor Inserido na Raiz\n\n");
    *raiz = novoNo;
  }
  else{
    No *aux = *raiz;
    while(aux != NULL){
      if(valor < aux->valor){
        printf("Andou para Esquerda\n");
        if(aux->esquerda == NULL){
          printf("Inseriu Valor\n");
          aux->esquerda = novoNo;
          break;
        }
        aux = aux->esquerda;
      }
      else{
        printf("Andou para Direita\n");
        if(aux->direita == NULL){
          printf("Inseriu Valor\n");
          aux->direita = novoNo;
          break;
        }
        aux = aux->direita;
      }
    }
  }
}

void emordem(No *raiz){
  if(raiz == NULL){
    return;
  }
  emordem(raiz->esquerda);
  printf("%i\n", raiz->valor);
  emordem(raiz->direita);
}

void preordem(No *raiz){
  if(raiz == NULL){
    return;
  }
  printf("%i\n", raiz->valor);
  emordem(raiz->esquerda);
  emordem(raiz->direita);
}

void posordem(No *raiz){
  if(raiz == NULL){
    return;
  }
  emordem(raiz->esquerda);
  emordem(raiz->direita);
  printf("%i\n", raiz->valor);
}

int main(void) {
  int qntd, valores, num = 1;
  No *raiz = NULL;

  printf("||  ====== Menu ======  ||\n");
  printf("|| Adicionar - Number 1 ||\n");
  printf("|| Em Ordem  - Number 2 ||\n");
  printf("|| Pré Ordem - Number 3 ||\n");
  printf("|| Pós Ordem - Number 4 ||\n");
  printf("||    Sair   - Number 0 ||\n");
  printf("|| ===================  ||\n");

while(num != 0){
  printf("\nMENU - Insira um Número: ");
  scanf("%i", &num);

  switch (num){
    
    case 1:
        printf("Quantos Valores Seram Adicionados: ");
        scanf("%i", &qntd);
        for(int i = 0; i < qntd; i++){
            printf("\nInsira o Valor: ");
            scanf("%i", &valores);
            printf("\n");
            insereNo(&raiz, valores);
        }
        break;
    
    case 2:
      printf("-- Imprimindo - Em Ordem: --\n");
      emordem(raiz);
        break;

    case 3:
      printf("-- Imprimindo - Pré Ordem: --\n");
      preordem(raiz);
      break;

    case 4:
      printf("-- Imprimindo - Pós Ordem: --\n");
      posordem(raiz);
      break;

    case 0:
      printf(" --- FIM --- ");
      break;
      
    default: 
      printf("Opção não disponivel!!!");
      break;
  }
}
  return 0;
}