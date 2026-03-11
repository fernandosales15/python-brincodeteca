""""

Introdução ao conceito de empacotamento e desempacotamento de listas.

Empacotamento: é o processo de agrupar vários valores em uma única estrutura de dados, 
como uma lista ou tupla. Por exemplo, quando criamos uma lista com vários elementos, 
estamos empacotando esses elementos juntos.

Desempacotamento: é o processo inverso, onde extraímos os valores individuais de uma 
estrutura de dados agrupada. Por exemplo, podemos desempacotar os elementos de uma lista 
em variáveis separadas.

"""

#empacotamento de diversos cargos em uma única variável do tipo lista.
cargos_engineer = ["Associate Software Enginner", "Software Engineer", "Senior Software Engineer"]
#desempacotamento de uma lista em variáveis separadas.
cargo1, cargo2 = cargos_engineer[0], cargos_engineer[1]
print(cargo1, cargo2)

#convencão de '_' indica que a variável não será utilizada, ou seja, é um placeholder.
_, _, cargo3 = cargos_engineer
print(cargo3)

#Armazena o primeiro cargo na variável o restante dos valores na variável 'resto_cargos' do tipo lista.
cargo1, *resto_cargos = cargos_engineer
print(cargo1)