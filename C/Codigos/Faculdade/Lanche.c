//Recebe o Código do lanche e a Quantidade desejada, logo após informa o total a se pagar.

#include <stdio.h>

int main(void) {
  int Cod, Qntd;

  printf("Insira o Código do Lanche:");
  scanf("%i", &Cod);

  printf("Insira a Quantidade:");
  scanf("%i", &Qntd);
  
  if(Cod == 1){
    printf("Total: R$ %.2f", Qntd * 4.0);
  } 
  else if(Cod == 2){
    printf("Total: R$ %.2f", Qntd * 4.5);
  } 
  else if(Cod == 3){
    printf("Total: R$ %.2f", Qntd * 5.0);
  } 
  else if(Cod == 4){
    printf("Total: R$ %.2f", Qntd * 2.0);
  } 
  else if(Cod == 5){
    printf("Total: R$ %.2f", Qntd * 1.5);
  } 
  else{
    printf("Código Não Reconhecido!");
  }
  return 0;
}