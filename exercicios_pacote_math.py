

##Exercicios

#Exercicio1: ##A megassena consiste em uma cartela de 60 números dentre os quais devemos acertar 6 (prêmio principal).
# Quantas combinações temos de 6 números nestes 60?
math.comb(60,6)


#Exercicio 2 - Calcule e exiba na tela a área do círculo de raio 4cm.
r=4
area = math.pi * r**2
print('A área é {:.2f} '. format(area))


#Exercício 3: - Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo qualquer em graus e mostre na tela o valor do seno, cosseno e tangente desse ângulo.#

a = float(input("Digite o ângulo que você deseja: "))
print("Seno: {:.2f}".format(math.sin(math.radians(a))))
print("Cosseno: {:.2f}".format(math.cos(math.radians(a))))
print("Tangente: {:.2f}".format(math.tan(math.radians(a))))