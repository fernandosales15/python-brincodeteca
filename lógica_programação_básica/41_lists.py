lista_a = ["Fernando", "Gabriela"]
lista_b = ["Luana"]
lista_a.extend(lista_b)
print(lista_a)

lista_c = lista_a.copy() #Copia o valor da lista 
lista_a[0] = "Fernandinho"
print(lista_a)
print(lista_c)

for nome in lista_c:
    print(nome, type(nome))


for nome in lista_a:
    print(lista_a.index(nome), nome)