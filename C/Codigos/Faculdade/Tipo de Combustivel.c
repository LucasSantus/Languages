//Recebe um valor, em seguinte informa sua escolha.

#include <stdio.h>

int main(void) {
  int Alcool = 0, Gasolina = 0, Diesel = 0, Escolha;
  
    printf("------- MENU -------\n");
    printf("  Alcool - Number 1\n");
    printf("Gasolina - Number 2\n");
    printf("  Diesel - Number 3\n");

  while(1)
  {
  scanf("%i", &Escolha);
    if(Escolha == 4){
        break;
    }
    else{
      if(Escolha == 1) Alcool++;
      else if(Escolha == 2) Gasolina++;
      else if(Escolha == 3) Diesel++;
    }
  }
  printf("MUITO OBRIGADO\n");
  printf("Alcool: %i\n",Alcool);
  printf("Gasolina: %i\n",Gasolina);
  printf("Diesel: %i\n",Diesel);
  
  return 0;
}