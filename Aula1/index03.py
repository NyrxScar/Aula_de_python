motorista_nome = input("Digite o nome do motorista: ")
motorista_sobrenome = input("Digite o sobrenome do motorista: ")
litros = float(input("Qnts litros foram abastecidos? " ))
valorDiesel = float(input("Qual valor do diesel por litro? "))
totalPagar = litros*valorDiesel
print(f"O motorista registrado como: {motorista_nome} {motorista_sobrenome} e o valor total a ser pago é de {totalPagar}")