lista = []
total = 0
for x in range(10):
    valor = int(input("Digite 1 valor de cada vez para uma lista de comprimeno 10: "))
    lista.append(valor)

for i in range(len(lista)):
    total = total + lista[i]

print(f"A lista é {lista}, e a soma dos valores da lista é {total}")
lista.sort()
print(f"A lista ordenada de maior para o menor é {lista}")