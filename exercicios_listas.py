# EXERCÍCIOS DE LISTAS - PYTHON BRASIL


# QUESTÃO 1:

# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# RESOLUÇÃO 1:
# numeros = [1,2,3,4,5]
# print(numeros)

# RESOLUÇÃO 2:
# numeros = []
# i = 1
# repeticoes = int(input("Quantos numeros você quer que a lista tenha? "))
#
# for i in range(repeticoes):
#     i += 1
#     numeros.append(input("Digite o {}º numero que deseja colocar na lista: ".format(i)))
#
# print(numeros)


# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 2:

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
# numeros = [12.4, 32.54, 29.7, 45.11, 54.89, 16.90, 14.34, 89.6, 95.96, 32.45]
# inverso = (numeros[::-1])
# print(inverso)

# --------------------------------------------------------------//--------------------------------------------------------------
# QUESTÃO 3:

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
#
# notas = []
# i = 1
# for i in range(4):
#     i += 1
#     notas.append(float(input("Digite a sua {}º nota: ".format(i))))
#
# somatorio = sum(notas)
# media = somatorio / i
# print(somatorio, media)

# --------------------------------------------------------------//--------------------------------------------------------------
# QUESTÃO 3:
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# vetor = "f, j, k, a, v, e, y, c, o, u"
# sem_espaco = vetor.replace(" ", "")
# sem_aspas = vetor.replace("\" \"", "" )
# consoantes = list("bcdfghjklmnpqrstvxwyz")
# vetor_consoantes = []
# cont_consoantes = []
# contador = 0
#
# for i in vetor:
#     if i in consoantes:
#         contador += 1
#
# print("Foram lidas um total de: {} consoantes.\nSendo elas: {}".format(contador, vetor_consoantes))


# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 4:
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# numeros = 0
# numeros_list = []
# pares = []
# impares = []
# i = 0
#
# for i in range(20):
#     i += 1
#     numeros = int(input("Digite o {}º número: ".format(i)))
#     numeros_list.append(numeros)
#     if numeros % 2 == 0:
#         pares.append(numeros)
#     else:
#         impares.append(numeros)
#
# lista_ordenada = sorted(numeros_list)
# print("O vetor total com os números é: {}\nO vetor dos numeros PARES é: {}\nO vetor dos números ÍMPARES é: {} ".format(lista_ordenada, pares, impares))

# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 5:

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# notas_list = []
# acima = []
# abaixo = []
# i = 0
# acima_media = 0
# abaixo_media = 0
#
# for b in range(3):
#     b += 1
#     notas_list.clear()
#     for i in range(4):
#         i += 1
#         nota = float(input("Digite a {}º nota do {} aluno(a): ".format(i, b)))
#         notas_list.append(nota)
#         soma = sum(notas_list)
#         media = soma / 4
#
#     if media >= 7.0:
#         acima_media += 1
#         acima.append(media)
#
#     else:
#         abaixo_media += 1
#         abaixo.append(media)
#
# print("O numero de alunos acima da média é: {}\nE as medias são: {}".format(acima_media,acima))
# print("O numero de alunos abaixo da média é: {}\nE as medias são: {}".format(abaixo_media, abaixo))

# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 6:

# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# i = 0
# numbers_list = []
# multiplicacao = 1
#
# while i <= 4:
#     i += 1
#     numero = int(input("Digite o {}º numero: ".format(i)))
#     numbers_list.append(numero)
#     multiplicacao *= numero
#
# soma = sum(numbers_list)
# print("A soma dos termos da lista é: {}\nA multiplicação dos termos da lista é: {}\nOs números da lista são: {}".format(soma, multiplicacao, numbers_list))

# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 7:

# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

# idade = 0
# altura = 0
# lista_idade = []
# lista_altura = []
#
# for i in range(5):
#     idade = int(input("Informe-nos a sua idade: "))
#     altura = float(input("Qual é a sua altura (em m)? "))
#     lista_idade.append(idade)
#     lista_altura.append(altura)
#
# inversa_idade = (lista_idade[::-1])
# inversa_altura = (lista_altura[::-1])
#
# print(lista_idade)
# print(inversa_idade)
# print(lista_altura)
# print(inversa_altura)

# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 8:

# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
# soma dos quadrados dos elementos do vetor.

# vetor_a = []
# numero = 0
# soma = 0
#
# for i in range(10):
#     numero = int(input("Digite um numero: "))
#     vetor_a.append(numero)
#     soma += (numero)**2
#
# print(soma)


# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 9:
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de
# 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

# vetor1 = [1,2,3,4,5]
# vetor2 = [6,7,8,9,10]
# vetor3 = list(zip(vetor1, vetor2))
#
# print(vetor3, end=" ")



# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 10:
# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# vetor1 = [1,2,3,4,5]
# vetor2 = [6,7,8,9,10]
# vetor3 = [11,12,13,14,15]
#
# vetor4 = list(zip(vetor1, vetor2, vetor3))
#
# print(vetor4)

# --------------------------------------------------------------//--------------------------------------------------------------

# QUESTÃO 11:
# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


