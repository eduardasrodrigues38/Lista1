#calculo IMC
#inserção dos dados do usuário
massa=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura em metros : "))
#calculo
imc=massa/(altura**2)
print("IMC = "+ str(imc))