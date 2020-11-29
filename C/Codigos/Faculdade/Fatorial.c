//Após receber um número, informa o fatorial recursvio e iterativo do mesmo.

#include <stdio.h>

int fatorialRecursivo(int n){
  if(n <= 1){
    return 1;
  }
  return n * fatorialRecursivo(n-1);
}

int fatorialIterativo(int n){
  int f = n;
  for( ; n > 1; n--){
    f *= (n-1);
  }
  return f;
}

int main(void) {
  int n;

  printf("\nInsira para Fatorar:");
  scanf("%i", &n);

  printf("\nFatorial - Recursivo: %i", fatorialRecursivo(n));
  
  printf("\nFatorial - Iterativo: %i", fatorialIterativo(n));

  return 0;
}