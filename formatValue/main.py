"""
Formatando valores

:f - Numero <Float>
:d - Numero <Integer>
:s - Texto <Integer>
:.5f (Quantidade de casas decimais
:[CARACTER][< ou > ou ^][QUANTIDADE][:f ou :d ou :s]

< - Direita
> - Esquerda
^ - Centro
"""

numero = 150
print(f'{numero:0>10}')
print(f'{numero:0<10}')
print(f'{numero:010}')
