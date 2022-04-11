##########################LISTA DE EXERCICIOS ATE AULA 5################################
######################################################################################


 ##Exercício 1 - Usando o terminal no VSCode, atribua uma string a uma variável.
 # Em seguida, imprima o conteúdo da variável usando a função print()

##Exercício 2 - O que acontece se você omitir um dos parênteses ou ambos numa instrução print?

##Exercício 3 -  Você pode usar um sinal de menos para fazer um número negativo como -2. 
# O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?


#Exercício 4: Escreva um programa que use inputs para solicitar ao usuário seu nome e,
#  em seguida, faça um cumprimento.
#saida esperada:
# Digite seu nome: Davi
# Olá Davi

#Exercício 5: Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número].

#Exercício 6: Inicialize o interpretador do Python no terminal do VSCode e use-o como uma calculadora.

#Quantos segundos há em 42 minutos e 42 segundos?

#Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

#10. Execute o código abaixo usando o terminal,ocorre algum erro? Como você pode corrigir?

'Eu comi ' + 34 + ' pastéis.'

#11 - Escreva um código em python que dada a palavra digitada pelo usuário ele calcule quantas letras a palavra possui.
#Dica: pesquise a função Len

palavra = input('entre com a palavra ')

print('Essa palavra possui', len(palavra) ,'letras')

# 12 - Exercício 4: Suponha que executamos as seguintes declaração por atribuição:
# Largura = 17
# Altura = 12.0
# Para cada uma das expressões a seguir, escreva o valor da expressão e o tipo (dovalor da expressão).
# 1. Largura//2 
# 2. Largura/2.0
# 3. Altura/3
# 4. 1 + 2 * 5

#Exercicio - 13 - Faça um Programa que solicite dois números ao usuário e imprima a soma.

#Exercicio - 14 - : Escreva um programa que solicite ao usuário as horas e o valor da
#  taxa por horas para calcular o valor a ser pago por horas de serviço. 
# Digite as horas: 35 
# Digite a taxa: 2.75 
# Valor a ser pago: 96.25

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
#  em graus Celsius. C = 5 * ((F-32) / 9).


#Exercicio - 15 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#  utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


##Exercicio - 16 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

######################
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
#######################
#Obs.: Salário Bruto - Descontos = Salário Líquido.

valor = int(input('Quanto voce ganha por hora: '))
horas = int(input('Numero de horas trabalhadas no mes: '))
salario = valor * horas
ir = (11/100.0 * salario)
print ('Imposto de renda: ',ir)
inss = (8/100.0 * salario)
print ('INSS: ',inss)
sind = (5/100.0 * salario)
print ('Sindicato: ',sind)
desc = ir + inss + sind
salarioL = salario - desc
print ('O desconto total do salario bruto(',salario,'R$)',
       'foi',desc,'\nO salario liquido ficou,',salarioL)



# Exercicio -17 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = input("Digite a quantidade de metros quadrados a serem pintados: ")
litros = metros/3

precoL = 80.0
capacidadeL = 18

latas = litros / capacidadeL
total = latas * precoL

print 'Você usara ',latas,'latas de tinta'
print 'O preco total é de: R$',total
