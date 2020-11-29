//Caso a senha seja diferente de 2002, ficará pedindo a senha até que seja a correta.

#include <stdio.h>

int main() {
  int Senha;
  
  printf("Insira a Senha");
  scanf("%i", &Senha);
  
  while(Senha != 2002){    
    printf("Senha Invalida\n");
    scanf("%i", &Senha);   
  }
  printf("Acesso Permitido\n");

  return 0;
}