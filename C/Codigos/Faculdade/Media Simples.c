//Recebe dois valores, logo após faz uma média simples com números já escolhidos.

#include <stdio.h>

int main(void) {
  float A,B,Media,Soma;
  
  printf("Insira o 1º Número:");
  scanf("%f", &A);

  printf("Insira o 2º Número:");
  scanf("%f", &B);
  
  A *= 3.5;
  B *= 7.5;
  
  Soma = A + B;
  
  Media = Soma/11;
  
  printf("Media = %.3f", Media);
  
  return 0;
}