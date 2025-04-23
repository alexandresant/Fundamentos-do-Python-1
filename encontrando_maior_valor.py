"""
Encontrar o maior valor em uma lista
novamente farei um código um pouco mais elaborado
com try except para verificar os valores digitados e tudo mais
Isso também pode ser feito através do método max(), porém por questões de aprendizado
decidi fazer usando if
"""
contador = 0
valor = 0
lista = []

indice = 0
while True:
    try:
        tamanho = int(input("Digite a quantidade de valores que deseja adicionar em sua lista: "))
        if tamanho <= 0:
            print("Digite um número inteiro maior que 0")
        
        else:
            break
    except:
        print("Digite um número inteiro")

for x in range(tamanho):
    while True:
        try:
            valor = int(input(f"Digite o {x + 1}° valor para a sua lista: "))
            lista.append(valor)
            break
        except:
            print(f"{valor} não é um número inteiro! Tente novamente.")

maior = lista[0]

for x in lista:
    if x > maior:
        maior = x
        indice = lista.index(x) + 1
print(f"O maio número da sua lista é {maior}, ele é o {indice}° número da lista")        