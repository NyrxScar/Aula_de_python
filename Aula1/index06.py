nome_cliente = input("Digite o seu nome (Cliente): ")
nome_vendedor = input("Digite o seu nome (Vendedor): ")
nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
valor_produto_desconto = valor_produto - valor_produto*0.2
comissao = valor_produto*0.04
print(f"{nome_cliente} possuindo 20% de desconto sobre o produto: '{nome_produto}' custando R${valor_produto} pagará R${valor_produto_desconto} ao vendedor {nome_vendedor} que ganhará 4% de comissão recebendo R${comissao}")

