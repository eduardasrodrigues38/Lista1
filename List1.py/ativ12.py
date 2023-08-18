#salario vendedor carros usados
#inserção dos dados do usuário
cQuant=int(input("Digite quantos carros você vendeu durante este mês: "))
vTotalVendas=float(input("Digite o valor total de suas vendas durante este mes: "))
sFixo=float(input("Digite o valor de seu salário fixo: "))
vComissao=float(input("Digite o valor de valor de sua comissão por carro vendido: "))
# Cálculo
vSalFinal = sFixo + vComissao*cQuant + ((5*vTotalVendas)/100)
print("Salario final: R$ "+str(vSalFinal))