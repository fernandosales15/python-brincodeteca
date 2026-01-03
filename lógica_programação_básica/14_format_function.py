# função format.` A função format permite formatar strings de maneira semelhante às f-strings.

cargo_junior = "Associate Software Engineer"
cargo_pleno = "Software Engineer"
cargo_senior = "Senior Software Engineer"
cargo_lead = "Lead Software Engineer"

# 1. Argumentos Nomeados (Named Arguments)
# Vantagem: A ordem dentro do format() não importa, desde que os nomes batam.
cargos_consolidados = "Carreiras na área de Eng. de Software: {ic3}, {ic4}, {ic5}, {ic6}.".format(
    ic3=cargo_junior, ic4=cargo_pleno, ic5=cargo_senior, ic6=cargo_lead) 

print("--- Exemplo Nomeado ---")
print(cargos_consolidados)

# 2. Argumentos Posicionais (Positional Arguments)
# O Python segue a ordem estrita: o primeiro {} pega o primeiro argumento, e assim por diante.
exemplo_posicional = "O cargo de entrada é {} e o seguinte é {}.".format(cargo_junior, cargo_pleno)

print("\n--- Exemplo Posicional ---")
print(exemplo_posicional)

# 3. A Regra de Ouro (Misturando os dois)
# Se você misturar, os posicionais (sem nome) DEVEM vir antes dos nomeados.
# Exemplo Válido: "Texto {} {nome}".format(variavel, nome="valor")
# Exemplo Inválido (Erro): "Texto {} {nome}".format(nome="valor", variavel)

print("\n--- Fim da Análise ---")

# Exemplo Válido: Parâmetros nomeados (Named Arguments).
# O Python sabe onde colocar cada um baseado no NOME {ic3} ou {ic6}.
print("Eu preciso começar como {ic3}, para um dia quem sabe ser {ic6}.".format(ic3=cargo_junior, 
ic6=cargo_lead))

#Exemplo númerico 2: Se um é numerado, todos os outros devem ser numerados também.
print("Carreira Starts: {1}, -> {2}. -> {0}. -> {3}.".format(cargo_pleno, cargo_senior, cargo_lead, cargo_junior))

# 4. Regra dos Índices (Tudo ou Nada)
# Você está certíssimo! Não se pode misturar chaves vazias {} com chaves numeradas {0}.
# Ou você numera TODAS as posições, ou deixa TODAS vazias (automático).
# Tentar misturar gera um erro: ValueError: cannot switch from manual field specification to automatic field numbering

# 5. Misturando índices com parâmetros nomeados
print("Carreira Mix: {0}, -> {pleno_engineer}.".format(cargo_junior, pleno_engineer=cargo_pleno))

# Feedback do Mentor:
print("\n--- Conclusão ---")
print("Fernando tem potencial para ser {cargo}? Resposta: {resp}".format(cargo="Associate Software Engineer", resp="Com certeza"))