//Recebe dois valores, logo após informa a multiplicação deste.

#include <stdio.h>

int main(void) {
  int A,B,Produto;
  
  printf("Insira o 1º Número:")
  scanf("%i",&A);

  printf("Insira o 2º Número:")
  scanf("%i",&B);
      
  Produto = A * B;
  
  printf("Produto = %i",Produto);

  return 0;
}