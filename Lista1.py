lista = [1, 2, 3, 4, 5]
print(f"A lista original é {lista}")
valor = int(input("Insira um valor para substituir o valor do meio da lista: "))
lista[2] = valor
print(f"A lista atual é {lista}")
del lista[4]
print(f"Lista atual {lista}")

