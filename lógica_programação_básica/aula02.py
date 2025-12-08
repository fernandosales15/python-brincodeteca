# Aula sobre os argumentos 'sep' e 'end' da função print.

# O argumento 'sep' (separator) define o caractere usado para separar os argumentos.
print(12, 34, sep='-') # Saída: 12-34
print(56, 78, sep='/') # Saída: 56/78
print(9, 10, sep=',')  # Saída: 9,10

# O argumento 'end' define o que é impresso no final da linha.
# O padrão é '\n' (uma quebra de linha).
print("Olá Fernando! Você será", end=" ") # Trocamos a quebra de linha por um espaço.
print("Associate Software Engineer") # Esta frase continuará na mesma linha da anterior.

"""
CRLF (Carriage Return, Line Feed) no VS Code são os caracteres de fim de linha, 
usados para indicar uma nova linha, sendo CRLF o padrão Windows (\r\n) e LF (\n) 
o padrão Unix/Linux/Mac, e você pode visualizar e mudar isso no canto inferior direito do 
VS Code (clicando em LF/CRLF) ou configurando a propriedade "files.eol" nas 
configurações (settings.json) para forçar um padrão para seu projeto ou globalmente. 
"""