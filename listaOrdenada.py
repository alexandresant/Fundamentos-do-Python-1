lista = []

for i in range(5):
    valor = int(input("Insira 1 valores a lista: "))
    lista.append(valor)

lista.sort()   
print(f"A lista ordenada do menor para o maior é {lista}")