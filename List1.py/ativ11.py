#custo de um carro novo ao consumidor
#inserção dos dados do usuário
cF=float(input("Digite o custo de fábrica do carro: "))
#percentuais
pDistri = 0.28
impostos = 0.45
# Cálculo do custo final ao consumidor
cDistri = cF * pDistri
cImpostos = cF * impostos
cFinal = cF + cDistri + cImpostos
print("Custo final: R$ "+str(cFinal))