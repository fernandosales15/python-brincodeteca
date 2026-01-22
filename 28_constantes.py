"""
Em python, podemos declarar constantes utilizando letras maiúsculas para o nome da variável.
Exemplo: PI = 3.14
Embora o Python não tenha suporte nativo para constantes, é o padrão usado pela comunidade.

"""

# Declaração de constantes em Python, valores comuns
PI = 3.14 # Valor aproximado de pi, algo utilizado em cálculos matemáticos
GRAVIDADE_TERRA = 9.81  # em m/s² - Utilizado para cálculos de física
VELOCIDADE_LUZ = 299792458  # em m/s - Velocidade da luz no vácuo

TEMPO_INICIO_ACRESCIMOS = 45 # Tempo em minutos para acréscimos em jogos de futebol
tempo_corrido_jogo_atual = 46

if tempo_corrido_jogo_atual >= TEMPO_INICIO_ACRESCIMOS:
    print("O jogo chegou no tempo de acréscimos!")
else:
    print("O jogo não chegou nos acréscimos ainda.")

velocidade_carro = 58 #km/h 
LIMITE_VELOCIDADE_RODOVIA = 120 #km/h
RANGE_RADAR_1 = LIMITE_VELOCIDADE_RODOVIA - 1 #Se chegar a 119 km/h, o radar notifica "dentro da velocidade".
RANGE_RADAR_2 = LIMITE_VELOCIDADE_RODOVIA + 2  #Se chegar a 122 km/h, o radar notifica "acima da velocidade".

if velocidade_carro >= RANGE_RADAR_2:
    print("Radar: Acima da Velocidade! Multa aplicada.")
elif velocidade_carro >= (RANGE_RADAR_1 - 60): # Os parênteses permitem quebrar a linha sem precisar da barra invertida (\)
    print("Radar: Dentro da velocidade permitida.")

else:
    print("Radar: Velocidade muito baixa! Cuidado com o fluxo de trânsito.")
