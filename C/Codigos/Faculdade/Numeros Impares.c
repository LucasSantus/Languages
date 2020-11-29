//Recebe um valor máximo, logo após informa apenas os números impares até esse máximo.

#include <stdio.h>

int main(void) {
  int valor, contador;
    
  printf("Insira um Valor: ");
  scanf("%i", &valor);
  contador = 1;
  
  while(contador <= valor){
    if(contador % 2 != 0){
      printf("%i\n", contador);
    }
    contador = contador + 1;
  }  
  return 0;
}