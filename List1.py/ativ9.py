#preço maçãs e babanas
#valores fixos
mVu= 1.30 #valor unitário das maças
bVkg=5 #valor por quilograma das babanas
#inserção dos dados do usuário
mQ=int(input("Digite a quantidade de maças: "))
bQ=int(input("Digite quantidade de babanas em kg: "))
#calculo
mVfinal=mQ*mVu
bVfinal=bQ*bVkg
cFinal=mVfinal+bVfinal
print("O valor a ser pago pelas maças é: "+str(mVfinal))
print("O valor a ser pago pelas bananas é: "+str(bVfinal))
print("O valor total dessa compra é: "+str(cFinal))