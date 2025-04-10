"""
Joga da velha em construção, primeiramente estou construindo a lógica das funções e 
testando, assim que tiver tudo ok eu vou construir o jogo todo.
Pode não parecer a melhor forma de se fazer isso, porém com estou no processo de aprendizagem
da linguagem essa foi uma forma que encontrei de ir aprendendo enquanto construo algo, uma forma
de colocar o conhecimento em prática.
"""

# Construi um tabuleiro 3x3 e preenche ele com números de 1 a 9
tabuleiro = [[i * 3 + x + 1 for x in range(3)] for i in range(3)]

#Função que imprime o tabuleiro (básico ainda irei melhorar isso, provavelmente farei algo usando hmtml e css)
def imprimeTabuleiro(tabuleiro):                
    for linha in range(3):
        for coluna in range(3):
            print(f"{tabuleiro[linha][coluna]}", end="")  
        print("", end="\n")

#apenas para colocar dados para testar as vitórias
tabuleiro[0][2] = "X"
tabuleiro[1][1] = "X"
tabuleiro[2][0] = "X"

imprimeTabuleiro(tabuleiro)

#Consulta todas as linhas do tabuleiro em busca de 3 valores iguais na mesma linha
for linha in range(3):
    for coluna in range(3):
        if tabuleiro [linha][coluna] == tabuleiro[linha][1] and tabuleiro[linha][coluna] == tabuleiro[linha][2]:
            print("Parabéns você ganhou!")
            break
#Consulta todas as colunas do tabuleiro em busca de 3 valores iguais na mesma coluna
for coluna in range(3):
    for linha in range(3):
        if tabuleiro[linha][coluna] == tabuleiro[1][coluna] and tabuleiro[linha][coluna] == tabuleiro[2][coluna]:
            print("Parabens você ganhou!")
            break
        
#Consulta as duas diagonais di tabuleiro em busca de 3 valores iguais na mesma diagonal
if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2] or tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]:
    print("Parabéns você venceu!")

        