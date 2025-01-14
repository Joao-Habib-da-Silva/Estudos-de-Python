import os

mensagens = []

nome = input("digite seu nome:")

while True:

    os.system('cls')
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("______________________")

    texto = input("digite a mensagem:")
    if texto == "fim":
        break
    mensagens.append ({
        'nome': nome,
        'texto':texto
    })
