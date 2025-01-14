#Oi meu nome é João Habib, estou no meu segundo dia de Python, e estou tentando pensar num jeito de fazer uma calculadora!
print("Olá, boa tarde! Esta será a primeira calculadora que o João Habib vai fazer! Agora vamos ao trabalho!")

tema = input("Gostaria de soma, subtração, multiplicação, divisão ou potenciação? ")
numero_de_itens = int(input("Ok, agora me diga com quantos números deseja fazer tal operação?:"))

numero_um = float(input("Digite o primeiro número de sua  operação seja qual for:"))
numero_dois = float(input("Digite o segundo número:"))
numero_tres = float(input("Digite aqui caso você escolheu operação de 3 números:"))

if tema == 'soma' and numero_de_itens == 2:
    print("Ok você escolheu adição!")
    print('{}+{}='. format(numero_um, numero_dois))
    print(numero_um + numero_dois)

elif tema == 'soma' and numero_de_itens == 3:
    print("Olha escolheu uma adição tripla!") 
    print('{}+{}+{}'.format(numero_um, numero_dois, numero_tres))
    print(numero_um + numero_dois +numero_tres)

elif tema == 'subtração' and numero_de_itens == 2:
    print("Ok você escolheu subtração!")
    print('{}-{}'.format(numero_um, numero_dois))
    print(numero_um - numero_dois)

elif tema == 'subtração' and numero_de_itens == 3:
    print("Ok, escolheu uma subtração tripla entao?")
    print('{}-{}-{}'.format(numero_um, numero_dois, numero_tres))
    print(numero_um - numero_dois - numero_tres)

elif tema == 'multiplicação' and numero_de_itens == 2:
    print("Ok, você escolheu multiplicação!")
    print('{}*{}'.format(numero_um, numero_dois))
    print(numero_um * numero_dois)

elif tema == 'multiplicação' and numero_de_itens == 3:
    print("Ok, escolheu uma multiplicação tripla!")
    print('{}*{}*{}'.format(numero_um, numero_dois, numero_tres))
    print(numero_um * numero_dois *  numero_tres)
   
elif tema == 'divisão'and numero_de_itens == 2:
    print("Ok, você escolheu divisão!")
    print('{}:{}'.format(numero_um, numero_dois))
    print(numero_um / numero_dois)

elif tema == 'divisão' and numero_de_itens == 3:
    print("Amigo, por enquanto não temos esse nivel ok?")
    
elif tema == 'potenciação' and numero_de_itens ==2:
    print("Ok você escolheu potenciação!")
    print('{}**{}'.format(numero_um, numero_dois))
    print(numero_um ** numero_dois)

elif tema == 'potenciação' and numero_de_itens == 3:
    print("Ok, uma potenciação tripla!")
    print('{}**({}*{})'.format(numero_um, numero_dois, numero_tres))
    numero_quatro = numero_dois * numero_tres
    print(numero_um ** numero_quatro)
