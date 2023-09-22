# EXERCÍCIOS RESOLVIDOS DAS LISTAS DO SITE - PYTHON BRASIL

#Resolvidos por: Dominique Morem.
#Em: 21 setembro 2023.

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 1:

# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

# print("Alô, Mundo!")

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 2:

# Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]".
# numero = int(input("Digite um número: "))
# print("\nO número informado foi {}.".format(numero))


#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 3:

# Faça um Programa que peça dois números e imprima a soma.

# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))

# soma = numero1 + numero2

# print("A soma entre {} e {} é: {}".format(numero1, numero2, soma))

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 4:

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# nota1 = float(input("Digite a sua média do primeiro bimestre: "))
# nota2 = float(input("Digite a sua média do segundo bimestre: "))
# nota3 = float(input("Digite a sua média do terceiro bimestre: "))
# nota4 = float(input("Digite a sua média do quarto bimestre: "))
#
# media = (nota1 + nota2 + nota3 + nota4) / 4
#
# print("\nA sua média é: {:.2f}".format(media))

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 5:

# Faça um Programa que converta metros para centímetros.
#OBSERVAÇÃO: Levando-se em consideração que 1 metro equivale a 100 centímetros.

# metros = float(input("Digite quantos metros deseja converter em centímetros: "))
# centimetros = metros * 100

# print("{:.2f} metros = {:.2f} centímetros".format(metros, centimetros))



#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 6:

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#OBSERVAÇÃO: A área de um círculo é dada pela seguinte fórmula: A = π * r²
#Onde:
# A - É a área,
# π - É pi (3,14159265358979323846)
# r² - É o raio da circunferência elevado ao quadrado

# raio = float(input("Por favor, digite o raio do seu círculo (em metros): "))
# area = (3.14159265358979323846) * (raio**2)
# print("A área de um círculo cujo raio é de: {:.2f} m\nÉ de: {:.2f} m²".format(raio,area))

#--------------------------------------------------------------//--------------------------------------------------------------


# QUESTÃO 7:

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#OBSERVAÇÃO: Sabendo que a área de um quadrado é lado x lado. Teremos...

# lado = float(input("Quantos cm tem o quadrado em questão? "))
# area = lado * lado
# dobro = area**2
# print("A área do quadrado é: {:.2f}\nE o dobro deste é: {:.2f}".format(area, dobro))


#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 8:

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# ganho_hora = float(input("Quanto você ganha por hora de trabalho (em R$)? "))
# horas_trabalhadas = int(input("Quantas horas você trabalhou esse mês? "))
# salario_total = ganho_hora * horas_trabalhadas
# print("O seu salário este mês é: \nR$ {:.2f}".format(salario_total))


#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 9:

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# OBSERVAÇÃO: Fórmula de conversão de Celsius para Fahrenheit: C = 5 * ((F-32) / 9).

# temp_fahrenheit = float(input("Quantos graus fahrenheit (°F) você deseja converter? "))
# celsius = 5 * ((temp_fahrenheit - 32) / 9)
# print("Em Fahrenheit, temos: {:.2f} °F\nEm Celsius, temos: {:.2f} °C".format(temp_fahrenheit, celsius))


#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 10:

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# OBSERVAÇÃO: Fórmula de conversão de Celsius para Fahrenheit: F = C x 1,8 + 32.

# temp_celsius = float(input("Quantos graus celsius (°C) você deseja converter? "))
# temp_fahrenheit = (temp_celsius * 1.8) + 32
# print("Em Celsius temos: {:.2f}\nEm Fahrenheit temos: {:.2f}".format(temp_celsius, temp_fahrenheit))

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 11:

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

# numero1 = int(input("Digite o primeiro número inteiro: "))
# numero2 = int(input("Digite o segundo número inteiro: "))
# num_real = float(input("Digite um número real: "))

# produto_dobro = (numero1 * 2) * (numero2 / 2)
# soma = (numero1 * 3) + num_real
# elevado_cubo = num_real**3

# print("Os números escolhido por você foram, respectivamente: \"{}\", \"{}\" e \"{}\".\nO produto do dobro do primeiro número com metade do segundo é: {:.2f}\nA soma do triplo do primeiro número com o terceiro resulta em: {:.2f}.\nO terceiro número elevado ao cubo resulta em: {:.2f}".format(numero1, numero2, num_real, produto_dobro, soma, elevado_cubo))

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 12:

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# altura = float(input("Por favor, digite a sua altura em metros: "))
# peso_ideal = (72.7*altura) - 58

# print("Se você mede: {:.2f} m.\nO seu peso ideal é: {:.2f} kg".format(altura, peso_ideal))


#--------------------------------------------------------------//--------------------------------------------------------------


# QUESTÃO 13:

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# genero = 0
# altura = float(input("Por favor, digite a sua altura em metros: "))
# print("Qual é o seu gênero?\n1 - Para Homem\n2 - Para Mulher")
# genero = int(input("Qual é o seu gênero? "))
# match genero:
#     case 1:
#         altura_homem = (72.7 * altura) - 58
#         print("\nVocê é um HOMEM, logo o peso ideal p/ a sua altura é:\n{:.2f} kg".format(altura_homem))
#     case 2:
#         altura_mulher = (62.1*altura) - 44.7
#         print("\nVocê é uma MULHER, logo o peso ideal p/ a sua altura é:\n{:.2f} kg".format(altura_mulher))
#     case _:
#         print("\nNumeração inexistente no campo de gêneros, por favor, tente novamente.")


#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 14:

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# peso_peixes = float(input("Digite quantos kg de peixe você pescou hoje: "))
# excesso = 51
# multa = 4.00 * (peso_peixes - 50)

# if peso_peixes >= excesso:
#     print("\nEXCESSO DETECTADO:\nVocê deverá pagar:\nR$ {:.2f} de multa.".format(multa))
# else:
#     print("\nSEM EXCESSO: Não há multas a pagar.")

#--------------------------------------------------------------//--------------------------------------------------------------


# QUESTÃO 15:

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# ganho_hora = float(input("Quanto você ganha por hora de trabalho (em R$)? "))
# horas_trabalhadas = int(input("Quantas horas você trabalhou esse mês? "))
# salario_bruto = ganho_hora * horas_trabalhadas
# imposto_renda = salario_bruto * (11/100)
# inss = salario_bruto * (8/100)
# sindicato = salario_bruto * (5/100)
# salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
#
# print("\nSobre o seu salário:\n\nSalário Bruto: R$ {:.2f}\nImposto de Renda: R$ {:.2f}\nINSS: R$ {:.2f}\nSindicato: R$ {:.2f}\nSalário Líquido: R$ {:.2f}".format(salario_bruto, imposto_renda, inss, sindicato, salario_liquido))

#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 16:


# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# import math
# area_pintada = float(input("Quantos m² possui a área a ser pintada em sua casa? "))
# litros_tinta = area_pintada / 3
# latas = math.ceil(litros_tinta / 18)
# preco = latas * 80.00
#
# if litros_tinta >= 18:
#     print("Você deverá comprar: {:.0f} latas de tinta.\nPois precisa de {:.2f} litros para pintar a área prevista.\nO total a pagar pelas {:.0f} latas é: R$ {:.2f}".format(latas, litros_tinta, latas, preco))
# else:
#     print("Você precisará de {:.2f} litro(s) de tinta.\nComo uma lata tem 18 l, apenas uma lata já lhe atenderá bem.\nO total a pagar pela 1 lata é: R$ {:.2f}".format(litros_tinta, preco))


#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 17:


# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# import math
#
# area_pintada = float(input("Quantos m² possui a área a ser pintada em sua casa? "))
# cobertura_tinta = area_pintada / 6
# so_latas = math.ceil(cobertura_tinta / 18)
# so_galoes = math.ceil(cobertura_tinta / 3.6)

# latas = cobertura_tinta // 18
# resto_galoes = cobertura_tinta % 18
# galoes_ini = resto_galoes / 3.6
# galoes_fin = math.ceil(galoes_ini + (galoes_ini * (10/100)))

# print("Variação de preços em 3 situações (precisa-se de {:.2f} litros):\n\nCaso SÓ LATAS sejam compradas:\nSerão necessárias: {:.0f} latas.\nTotalizando: R${:.2f}".format(cobertura_tinta, so_latas, so_latas*80))
# print("\nCaso SÓ GALÕES sejam comprados:\nSerão necessários: {:.0f} galões.\nTotalizando: R${:.2f}".format(so_galoes, so_galoes*25))
# print("\nCaso opte MESCLAR OS DOIS, serão necessários: {:.0f} latas e {:.0f} galões.\nTotalizando: R$ {:.2f}".format(latas, galoes_fin, (latas*80)+(galoes_fin*25)))



#--------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 18:

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# tamanho_arquivo = float(input("Qual o tamanho do arquivo que deseja download (em MB)? "))
# velocidade_link = float(input("Qual é a velocidade do link de Internet que você escolheu (em Mbps)? "))

# segundos = tamanho_arquivo / (velocidade_link / 8)
# minutos = segundos // 60
# segundos2 = segundos % 60

# print("O tempo aproximado é de:\n{:.2f} minutos e {:.0f} segundos".format(minutos, segundos2))
