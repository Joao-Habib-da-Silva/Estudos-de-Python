

notas = []
contador = 1
while contador <=3:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    print("quantidade de notas", len(notas))
    contador = contador +1

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O codigo do aluno", codigo_aluno, "tirou a nota", nota)