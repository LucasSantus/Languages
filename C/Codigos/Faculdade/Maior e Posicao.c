//Recebe 10 valores, logo após informa o maior número, em qual posição ele se encontra.

#include <stdio.h>
int Maiorn(){
    int Posicao=0, Contador, Maior, NumPosicao, Num=0;

    for(Contador=1; Contador<=10; Contador++){
        scanf("%i", &Maior);
        Posicao++;
        if(Maior>Num){
            NumPosicao=Posicao;
            Num=Maior;
        }
    }
    printf("%i\n",Num);
    printf("%i\n",NumPosicao);

    return 0;
}