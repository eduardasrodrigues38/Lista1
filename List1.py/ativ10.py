#Idade em dias
#inserção dos dados do usuário
iA=int(input("Digite a sua idade em anos: "))
iM=int(input("Há quantos meses fez aniversário? "))
iD=int(input("Digite a quantidade de dias se passaram desde seu aniversário (sem contar os anos e meses): "))
#coversões
resp=(iA*365)+(iM*30)+iD
print("Sua iade em dias é: "+str(resp)+" dias.")