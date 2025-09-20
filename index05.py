nome_paciente = input("Digite o nome do(a) paciente: ")
ano_nascimento = int(input("Digite o ano do seu nascimento:"))
altura = float(input("Digite sua altura:"))
peso = float(input("Digite o seu peso:"))
idade = 2025-ano_nascimento
imc = peso/altura**2
print(f"O(a) paciente {nome_paciente} possui ou vai fazer {idade} anos de idade, com IMC {imc:.2f}")

