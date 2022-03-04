from math import *

print("Escolha o tipo da função, para isso  digite: 1 para uma função do tipo: x / 2 para uma função do tipo: x^ / 3 para uma função do tipo cos(x) (em graus) / digite 4 para uma função do tipo sen(x) (em graus). ")
print("                        ") #só pra criar uma quebra de linha

selecao = int(input("tipo da função: "))

if (selecao == 2): #caso a escolha seja função do tipo x^ (2) pedirá o valor do expoente
 q       = float(input("Defina o valor do expoente de x: "))

m       = float(input("Defina o valor que multiplica a função: "))
a       = float(input("Defina o limite inferior: "))
b       = float(input("Defina o limite superior: "))
N       = 1000

def funcao_selec(x, selecao):
    if (selecao == 1):
              y=m*x
    elif (selecao == 2):
        y=m*x**q
    elif (selecao == 3):
        y=m*cos(x)
    elif (selecao == 4):
        y=m*sin(x)

    return y

def integral(a,b,N): #cáculo da integral
    valor  = (b-a)/N
    valor2 = 0.5 * (funcao_selec(a, selecao)+funcao_selec(b, selecao))
    for i in range(1,N):
        valor2 +=(funcao_selec((a+i * valor), selecao))
    return valor*valor2

print("                        ") #só pra criar uma quebra de linha
print("Resultado: ", )
print(integral(a,b,N))