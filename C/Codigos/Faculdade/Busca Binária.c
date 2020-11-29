//Para funcionar, é necessário encher o vetor de [TAM] posições.

#include <stdio.h>

#define TAM 5

int PesquisaBinaria (int vet[], int chave, int Tam){
  int inicio = 0;  
  int fim = Tam-1;
  int meio;
  while (inicio <= fim){
    meio = (int)(inicio + fim)/2;
    if (chave == vet[meio]){
      return meio;
    }
    if (chave < vet[meio]){
      fim = meio-1;
    }
    else{
      inicio = meio+1;
      }
    }
  return -1; 
}

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

  int vetor[TAM], busca, qntd, posicao = 0, i;

  printf("\nQuantos Números Seram Adicionados: ");
  scanf("%i", &qntd);

  for(i = 0; i < qntd; i++){

    printf("\nAdicione o %iº Número: ", i+1);
    scanf("%i", &vetor[i]);
  }

  printf("\nInsira um Número Para Fazer a Busca: ");
  scanf("%i", &busca);

  bubbleSort(vetor);

  int resultado = PesquisaBinaria(vetor, busca, qntd);

  printf("Número [%i] encontrado na Posição: %i", busca, resultado);
  
  return 0;
}