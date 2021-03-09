def calcular_imc(peso, altura):
    try:   
        print("\n -------------------- \n")
        print("Calculando IMC...\n")

        total_imc = peso/(altura*altura)

        print(total_imc)
        
        if total_imc < 16:
            print("Magreza Grave\n")
        
        elif total_imc >= 16 and total_imc < 17:
            print("Magreza Moderada\n")

        elif total_imc >= 17 and total_imc < 18.5:
            print("Magreza Leve")

        elif total_imc >= 18.5 and total_imc < 25:
            print("Saudável")

        elif total_imc >= 25 and total_imc < 30:
            print("Sobrepeso")

        elif total_imc >= 30 and total_imc < 35:
            print("Obesidade Grau I")

        elif total_imc >= 35 and total_imc < 40:
            print("Obesidade Grau II (Severa)")

        elif total_imc > 40:
            print("Obesidade Grau III (Mórbida)")   

        else:
            print("Faliceu")                 
        
    except:
        print("Valores Inválidos!")