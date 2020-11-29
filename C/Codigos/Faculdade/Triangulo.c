//Recebe três valores, logo após informa qual triângulo seria.

#include <stdio.h>

int main(){
  int a, b, c, temp;

  scanf("%i %i %i", &a, &b, &c);

  if (a < b){
    temp = a;
    a = b;
    b = temp;
  }
  if (b < c){
    temp = b;
    b = c;
    c = temp;
  }
  if (a < b){
    temp = a;
    a = b;
    b = temp;
  }
  else if (a * a == b * b + c * c){
        printf("TRIÂNGULO RETANGULO\n");
  }
  else if (a * a > b * b + c * c){
    printf("TRIÂNGULO OBTUSANGULO\n");
  }
  else if (a * a < b * b + c * c){
    printf("TRIÂNGULO ACUTANGULO\n");
  }
  if (a == b && b == c){
    printf("TRIÂNGULO EQUILATERO\n");
  }
  else if (a == b || b == c){
    printf("TRIÂNGULO ISOSCELES\n");
  }
  else{
    printf("NÃO É TRIÂNGULO\n");
  }
  

  return 0;
}