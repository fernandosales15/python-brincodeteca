"""
Interpolação básica de strings

s = string
d & f = números (int e float)
b = booleano (True ou False)
#a = ascii (representação ascii do objeto)
x & X = números em hexadecimal (base 16) (ABCDEF0123456789)
"""

nome = "Fernando" #Tipo de Dado: String (str) 
tempo_no_projeto = 1233.0223232 #Tipo de Dado: Float (float)
cargo_atual = "Associate Software Engineer" 
frase_completa = "O %s está no cargo de %s há %.2f dias." % (nome, cargo_atual, tempo_no_projeto)
print(frase_completa)

# %a chama a função ascii() (similar ao repr()). Não é uma letra aleatória.
# %04X converte para HeXadecimal, Maiúsculo, preenchendo com 0 até ter 4 casas.
print("O número hexadecimal de %a é %04X" % (2000, 2000))
