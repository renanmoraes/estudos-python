"""
Manipulando string

- String indices
- Fatiamento de strings [inicio:fim:passo]
- Funcoes

built-in =>
len => Retorna o tamanho da string
abs =>
type =>
print =>

"""
# Pegue para mim a posicao 4
texto = "Amo desenvolver em Python"
print(texto[4])

# Pegue para mim da posicao 4 ate a 14
texto_fatiamento = texto[4:14]
print(texto_fatiamento)

# Pegue para mim da posicao 0 ate a final pulando de 3 em 3
texto_pulado = texto[0:-1:3]
print(texto_pulado)

# Retorna o tamanho de caracteres do item
print(len(texto))