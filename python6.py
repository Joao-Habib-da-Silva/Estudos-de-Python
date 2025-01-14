#estudo de como fazer diferentes tipos de listas
primeiro_numero = int(input("Fale o primeiro número da lista:"))
segundo_numero = int(input("Fale o segundo número da lista:"))
terceiro_numero = int(input("Fale o terceiro número da lista:"))
quarto_numero = int(input ("Fale o quarto número da lista:"))
quinto_numero = int(input ("Fale o quinto número da lista:"))
sexto_numero = int(input ("Fale o sexto número da lista:"))
setimo_numero = int(input ("Fale o sétimo número da lista:"))

lista = [primeiro_numero, segundo_numero, terceiro_numero, quarto_numero, quinto_numero, sexto_numero, setimo_numero]
lista.sort(key=int)
print(lista)