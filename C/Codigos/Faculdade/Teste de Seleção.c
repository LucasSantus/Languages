//Apenas um teste com valores.

#include <stdio.h>

int main(void) {
  int A, B, C, D;

  printf("Insira um Valor para A:");
  scanf("%i", &A);
  
  printf("Insira um Valor para B:");
  scanf("%i", &B);

  printf("Insira um Valor para C:");
  scanf("%i", &C);

  printf("Insira um Valor para D:");
  scanf("%i", &D);

  if(B > C ){
    if(D > A){
      if(C + D > A + B){
        printf("Valores Aceitos");
      }
      else{
        printf("Valores Não Aceitos");
      } 
    }
  }  
  else{
    printf("Valores Não Aceitos");
  }
  return 0;
}