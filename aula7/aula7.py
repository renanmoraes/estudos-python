nome = 'Renan'
idade = 28
altura = 1.8
e_maior = idade > 18
peso = 102.5
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc))
print('{1} tem {0} anos de idade e seu imc é: {2:.2f}'.format(nome, idade, imc))
print('{n} tem {mc} anos de idade e seu imc é: {mc:.2f}'.format(n=nome, i=idade, mc=imc))