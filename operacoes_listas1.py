""""
Imagine uma lista - não muito longa, não muito complicada, apenas uma lista simples que contém alguns números inteiros. Alguns desses números podem ser repetidos, e essa é a pista. Não queremos repetições. Queremos que eles sejam removidos.

Sua tarefa é escrever um programa que remova todas as repetições de números da lista. O objetivo é ter uma lista na qual todos os números não aparecem mais de uma vez.

Nota: suponha que a lista de origem seja codificada dentro do código - você não precisa inseri-la no teclado. Claro, você pode melhorar o código e adicionar uma parte que possa conversar com o usuário e obter todos os dados dele.

Dica: recomendamos que você crie uma nova lista como uma área de trabalho temporária. Você não precisa atualizar a lista in situ.

Não fornecemos dados de teste, pois isso seria muito fácil. Você pode usar o nosso esqueleto.
"""
lista1 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista2 = []
for i in lista1:
    if i not in lista2:
        lista2.append(i)

print(lista2)