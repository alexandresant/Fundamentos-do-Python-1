var1 = int(input("Digite um valor: "))
var2 = int(input("Digite um valor: "))
var3 = int(input("Digite um valor: "))
var4 = int(input("Digite um valor: "))
var5 = int(input("Digite um valor: "))
maior1 = 0
maior2 = 0
maior3 = 0
maior4 = 0
maior5 = 1
#Encontrando o maior número
if var1 > var2 and var1 > var3 and var1 > var4 and var1 > var5:
    maior5 = var1
    a, b, c, d = var2, var3, var4, var5
if var2 > var1 and var2 > var3 and var2 > var4 and var2 > var5:
    maior5 = var2
    a, b, c, d = var1, var3, var4, var5
if var3 > var1 and var3 > var2 and var3 > var4 and var3 > var5:
    maior5 = var3
    a, b, c, d = var1, var2, var4, var5
if var4 > var1 and var4 > var2 and var4 > var3 and var4 > var5:
    maior5 = var4
    a, b, c, d = var1, var2, var3, var5 
if var5 > var1 and var5 > var2 and var5 > var3 and var5 > var4: 
    maior5 = var5 
    a, b, c, d = var1, var2, var3, var4

#Encontrando o segundo maior número
if a > b and a > c and a > d:
    maior4 = a
    a1, b1, c1 = b, c, d
if b > a and b > c and b > d:
    maior4 = b
    a1, b1, c1 = a, c, d
if c > a and c > b and c > d:
    maior4 = c
    a1, b1, c1 = a, b, d
if d > a and d > b and d > c:
    maior4 = d
    a1, b1, c1 = a, b , c

#Encontrando o terceriro maior
if a1 > b1 and a1 > c1:
    maior3 = a1
    a2, b2 = b1, c1
if b1 > a1 and b1 > c1:
    maior3 = b1
    a2, b2 = a1, c1
if c1 > a1 and c1 > b1:
    maior3 = c1
    a2, b2 = a1, b1

#Encontrando o quarto maior e o menor
if a2 > b2:
    maior2 = a2
    maior1 = b2
if b2 > a2:
    maior2 = b2
    maior1 = a2

print(maior1, maior2, maior3, maior4, maior5)