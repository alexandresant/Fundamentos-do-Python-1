"""
Joga da velha em construção, primeiramente estou construindo a lógica das funções e 
testando, assim que tiver tudo ok eu vou construir o jogo todo.
Pode não parecer a melhor forma de se fazer isso, porém com estou no processo de aprendizagem
da linguagem essa foi uma forma que encontrei de ir aprendendo enquanto construo algo, uma forma
de colocar o conhecimento em prática.
"""
import os

print("""   Bem vindo ao jogo da velha!
             ___|___|___
             ___|___|___
                |   |
""")
iniciar_jogo = ""
simbolo_jogador1 = ""
simbolo_jogador2 = ""
jogador1 = ""
jogador2 = ""
tabuleiro = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

#Função que coleta os nomes e o símbolo de cada jogador.
def nomes_jogadores():
    while True:
        jogador1 = input("Digite o nome do jogador 1: ")
        if not jogador1.strip():
            print("O nome está vazio.")
        else:
            break
    while True:
        simbolo_jogador1 = input(f"Certo {jogador1} agora escolha X ou O? ").upper()
        if simbolo_jogador1 == "X" or simbolo_jogador1 == "O":
            print(f"Muito bem {jogador1}, seu símbolo é {simbolo_jogador1}.")
            break   
        else:
            print(f"{jogador1}, digite um símbolo válido X ou O") 

    if simbolo_jogador1 == "X":
        simbolo_jogador2 = "O"
    else:
        simbolo_jogador2 = "X"
      
    while True:
        jogador2 = input("Digite o nome do jogador 2: ")
        if not jogador2.strip():
            print("O nome está vazio.")
        else:
            print(f"Muito bem {jogador2}, seu símbolo é {simbolo_jogador2}.")
            break
    return jogador1, jogador2, simbolo_jogador1, simbolo_jogador2

#Função que imprime o tabuleiro (básico ainda irei melhorar isso, provavelmente farei algo usando hmtml e css)
def imprime_tabuleiro(tabuleiro):  
   # os.system('cls' if os.name == 'nt' else 'clear')              
    for linha in range(3):
        print(f"{tabuleiro[linha][0]} | {tabuleiro[linha][1]} | {tabuleiro[linha][2]}") 
        if linha < 2:
            print("__________")

def consulta_vitoria(tabuleiro, jogador1, jogador2, simbolo_jogador1):
    #Consulta todas as linhas do tabuleiro em busca de 3 valores iguais na mesma linha
    for linha in range(3):
        if tabuleiro [linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2]:
            if tabuleiro[linha][0] == simbolo_jogador1:
                    print(f"Parabéns {jogador1} você ganhou!")
                    return True
            else: 
                print(f"Parabéns {jogador2} você ganhou!")  
                return True  

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] ==tabuleiro[2][coluna]:
            if tabuleiro[0][coluna] == simbolo_jogador1:
                print(f"Parabéns {jogador1} você ganhou!")
                return True
            else: 
                print(f"Parabéns {jogador2} você ganhou!")
            return True
                        
    #Consulta as duas diagonais di tabuleiro em busca de 3 valores iguais na mesma diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        if tabuleiro[1][1] == simbolo_jogador1:
            print(f"Parabéns {jogador1} você ganhou!")
            return True
        else: 
            print(f"Parabéns {jogador2} você ganhou!")
            return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        if tabuleiro[1][1] == simbolo_jogador1:
            print(f"Parabéns {jogador1} você ganhou!")
            return True
        else: 
            print(f"Parabéns {jogador2} você ganhou!")
            return True
        
def consultar_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula != "X" and celula != "O":
                return False
    print("Deu Velha! O jogo empatou.")
    return True


def jogada(tabuleiro, jogador, simbolo_jogador):
    while True:
        try:
            jogada = int(input(f"{jogador}, Digite o número da posição para realizar a sua jogada: "))
            if jogada < 1 or jogada > 9:
                print("Digite um número entre 1 e 9")
                continue
        except ValueError:
            print("Digite um número válido entre 1 e 9!")
            continue
            
        linha = (jogada - 1) // 3
        coluna = (jogada -1 ) % 3
        if tabuleiro[linha][coluna] != "X" and tabuleiro[linha][coluna] != "O":
            tabuleiro[linha][coluna] = simbolo_jogador
            print(f"{jogador} fez a jogada na posição {jogada}")
            break
        else:
            print(f"{jogador} digite outro número essa casa já esta ocupada")

        

while True:
    try:
        iniciar_jogo = int(input("Digite a opção desejada, 1 para iniciar o jogo e 2 para sair: "))   
    except:
        print("Digite uma opção válida 1 ou 2!")
   
    
    if iniciar_jogo == 1:
        fim_jogo = False
        tabuleiro = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
                     
        jogador1, jogador2, simbolo_jogador1, simbolo_jogador2 = nomes_jogadores()
        while not fim_jogo:
            imprime_tabuleiro(tabuleiro)

            jogador = jogador1
            simbolo_jogador = simbolo_jogador1

            jogada(tabuleiro, jogador, simbolo_jogador)
            
            if consulta_vitoria(tabuleiro, jogador1, jogador2, simbolo_jogador1):
                break
            if consultar_empate(tabuleiro):
                break
          
    
            imprime_tabuleiro(tabuleiro)
            jogador = jogador2
            simbolo_jogador = simbolo_jogador2
            jogada(tabuleiro, jogador, simbolo_jogador)
            
            if consulta_vitoria(tabuleiro, jogador1, jogador2, simbolo_jogador1):
                break 
            if consultar_empate(tabuleiro):
                break

    elif iniciar_jogo == 2:
        print("Que pena que não quer mais jogar, volte logo!")
        break
    else: 
        print("Digite um número inteiro válido entre 1 e 2")    
                  