//Recebe três valores, logo após informa o salário do funcionário.

#include <stdio.h>

int main(void) {
  int N, HorasTrab;
  float ValorHora, Salario;
  
  printf("Insira o Número do Funcionário: ");
  scanf("%i", &N);

  printf("Insira a Quantidade de Horas Trabalhadas: ");
  scanf("%i", &HorasTrab);

  printf("Insira o Valor por Hora: ");
  scanf("%f", &ValorHora);
  
  Salario = ValorHora * HorasTrab;
  
  printf("Número do Funcionário:  %i\n", N);
  printf("Salário: U$ %.2f", Salario);
   
  return 0;
}