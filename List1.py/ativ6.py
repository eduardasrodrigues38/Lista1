#volume e area de uma esfera
#inserção dos dados do usuário
raio=float(input("Digite o raio da esfera: "))
pi=3.14
#calculo
volume=(4/3)*pi*(raio**3)
area=4*pi*(raio**2)
print("volume: "+str(volume))
print("área: "+str(area))
