#quantos azulejos são necessários para azulejar uma parede
#inserção dos dados do usuário
aP=float(input("Digite a altura da parede em metro : "))
lP=float(input("Digite a largura da parede em metro : "))
aA=float(input("Digite a altura do azulejo em metro : "))
lA=float(input("Digite a largura do azulejo em metro : "))
#calculo de area
areaP=aP*lP
areaA=aA*lA
#coversão final
convert=areaP/areaA
print(convert)
