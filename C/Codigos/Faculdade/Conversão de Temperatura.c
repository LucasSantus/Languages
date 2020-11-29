//Recebe um número de entrada e o converte em horas, minutos e segundos. 

#include <stdio.h>

int main(void) {
  int Num, Hora, Minuto, Segundo;
  
  printf("Insira um Valor para Converter: ");
  scanf("%i", &Num);
  
  Hora = Num/3600;
  Minuto = (Num%3600)/60;
  Segundo = (Num%3600)%60;

  printf("%i:%i:%i", Hora, Minuto, Segundo);
  
  return 0;
}