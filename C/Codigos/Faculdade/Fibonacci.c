#include <stdio.h>

int fibonacciRecursivo(int n){
  if(n < 2){
    return n;
  }
  return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2);
}

int fibonacciIterativo(int n){
  int total, a = 1, b = 0, c;
  for(int max = 0 ; max < n; max++){
    c = a + b;
    a = b;
    b = c;
  }
  return c;
}

int main(void) {
  int n;
  printf("Digite um Número: ");
  scanf("%i", &n);
  printf("\nSérie de Fibonacci - Iterativo: %i", fibonacciIterativo(n));
  printf("\nSérie de Fibonacci - Recursivo: %i", fibonacciRecursivo(n));

  return 0;
}