lista = [50, 65, 32, 3, 4, 8, 1, 0]
cont = 0
while True:     
    try:
        valor = int(input("Digite uma valor para descobrir se ele está na lista:"))
        if valor in lista:
            print(f"Parabéns você acertou, {valor} está na lista!!!")
            posicao = lista.index(valor) + 1
            print(f"Ele é o {posicao}° valor da lista")
            break
        else:
            print(f"{valor} não está na lista tente novamente!")
    except:
        print(" Digite um núnero inteiro válido!")
        
