print("Números Primos")

total = 0

num = int(input("Insira um Número: "))

for a in range(1, num + 1):
    if num % a == 0:
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(a), end="")
print("\n\033[mO número {} foi divisivel {} vezes".format(num, total))

if total == 2:
    print("Por isso ele é Primo!")
else:
    print("Por isso ele não é Primo!")
