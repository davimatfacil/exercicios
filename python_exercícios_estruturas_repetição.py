# -*- coding: utf-8 -*-
"""Python Exercícios Estruturas Repetição


# Exercício 1

Ler 5 notas e informar a média

## For
"""

nota = media = soma = 0

print(nota, media, soma)

for _ in range(1, 6):
  nota = float(input('Digite a nota '))
  soma += nota

print(soma)

media = soma / 5
print('A média é ', media)

"""## While"""

nota = soma = 0
numero = 1
while numero <= 5:
  nota = float(input('Digite a nota:'))
  soma += nota
  numero += 1
print('A média é ', soma / 5)

"""# Exercício 2

Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)

## For
"""

for i in range(1, 11):
  print('3 x {} = {}'.format(i, 3 * i))

"""## While"""

numero = 1
while numero <= 10:
  print('3 x {} = {}'.format(numero, 3 * numero))
  numero += 1