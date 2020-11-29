//Controle o tamanho do vetor pelo [TAM]

#include <stdio.h>

#define TAM 10

void bubbleSort (int v[TAM]) {
    int a, b, aux;
    for (a=TAM-1; a>=1; a--) {
        for (b=0; b<a; b++) {
            if (v[b]>v[b+1]) {
                aux = v[b];
                v[b] = v[b+1];
                v[b+1] = aux;
            }
        }
    }
}

int main(void) {
  int v[TAM];

  for(int i = 0; i < TAM; i++){
    printf("Insira o %iº Valor: ", i+1);
    scanf("%iº", &v[i]);
  }

  printf("---- Antes do Bubble Sort ----\n");

  for(int i = 0; i < TAM; i++){
    printf(" %i", v[i]);
  }
  bubbleSort(v);

  printf("\n---- Depois do Bubble Sort ----");
  
  for(int i = 0; i < TAM; i++){
    printf(" %i", v[i]);
  }
  return 0;
}