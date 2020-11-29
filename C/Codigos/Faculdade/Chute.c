//Chute um número até acertar.

#include <stdio.h>

int main(void) {
  int Num = 9, X;
  
  do
  {
    printf("Informe seu Chute: \n");
    scanf("%i", &X);
    
    if(X > Num){
      printf("Tente um Número Menor.\n");
    }
    if(X < Num){
      printf("Tente um Número Maior.\n");
      
    }
  } while(Num != X);

  printf("Acertou\n");
  return 0;
}