nome_aluno = input("Digite o nome do(a) aluno(a): ")
nome_professora = input("Digite o nome da professora: ")
nota1 = float(input("Digite sua primeira nota: " ))
nota2 = float(input("Digite sua segunda nota: " ))
nota3 = float(input("Digite sua terceira nota: " ))
media = (nota1+nota2+nota3)/3
print(f"O aluno(a) nomeado(a) como {nome_aluno} na aula da docente {nome_professora} possui uma média de {media:.2f} ")