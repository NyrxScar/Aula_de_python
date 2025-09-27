lista = ["Nyrx", "Gab", "Willian", "Mia"]
print(type(lista))
# print(lista[1])
lista2 = ("Nyrx", "Gab", "Willian", "Mia")
print(type(lista2))
lista.append("Alex")
print(lista)
del lista[0]
print(lista)

valor = 0
while valor<10:
    valor+=1
    print(valor)
print(valor)

x = 0

while x < 10:
    print(f"O valor de x nesta iteração é: {x}")
    print("X ainda é menor que 10, somando 1 a x")
    x += 1
else:
    print("Loop Concluído")
print(x)