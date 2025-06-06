"""
A idéia era fazer um algoritimo que ordenasse lista usando Bubblesort, 
onde o usuário digitaria o tamanho da lista e os valores. Porém eu acabei incrementando um pouco
o código, adicionando alguns travas de segurança que obrigam o usuário a digitar os valores 
corretos e caso ele digite letras o números negativos para o tamanho da lista o software avisa
e solicita que seja digitado os valores corretos. 
"""

lista = []
contador = 0
while True:
    num = input("Quantos números deseja adicionar a lista: ")
    try:
        num = int(num)
        if num <= 0:
            print("Digite um valor inteiro maior que 0!")
        else:
            break
    except ValueError:
        print("O Valor digitado não é um número inteiro!")

for x in range(num):
    while True:
        valor = input(f"Digite o {x + 1}° número inteiro para a lista: ")
        try:
            valor = int(valor)
            lista.append(valor)
            break
        except:
            print("O valor digitado não é um inteiro, tente novamente!")

print(f"A lista atual é {lista}")
ordenada = True
while  ordenada:
    ordenada = False
    for x in range(len(lista) -1):
        if lista[x] > lista[x + 1]:
            loop3 = True
            lista[x], lista[x + 1] = lista[x + 1], lista[x]
            contador += 1
print(f"A lista ordenada pelo método Bublesorte ficou assim {lista}")
print(f"Foram precisos {contador} etapas!")