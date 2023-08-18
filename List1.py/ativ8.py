#Movimento Uniformemente Variado
#valores fixos
s0=2
v0=3
a=10
#inserção dos dados do usuário
t=int(input("Digite o tempo em segundos: "))
#calculo
s=s0+v0*t+0.5*a*t**2
print("O espaço s percorrido é: "+str(s))