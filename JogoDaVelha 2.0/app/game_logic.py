"""
Joga da velha em construção, primeiramente estou construindo a lógica das funções e 
testando, assim que tiver tudo ok eu vou construir o jogo todo.
Pode não parecer a melhor forma de se fazer isso, porém com estou no processo de aprendizagem
da linguagem essa foi uma forma que encontrei de ir aprendendo enquanto construo algo, uma forma
de colocar o conhecimento em prática.
"""
from flask import session

iniciar_jogo = ""
simbolo_jogador1 = ""
simbolo_jogador2 = ""
jogador1 = ""
jogador2 = ""



def inicializar_tabuleiro():
    tabuleiro = []           
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append('')
        tabuleiro.append(linha)
        session['tabuleiro'] = tabuleiro  # Salva o tabuleiro na sessão
    return tabuleiro

#Função que coleta os nomes e o símbolo de cada jogador.
def nomes_jogadores(jogador1, jogador2, simbolo_jogador1, simbolo_jogador2):
    session['jogador1'] = jogador1
    session['jogador2'] = jogador2
    session['simbolo_jogador1'] = simbolo_jogador1
    session['simbolo_jogador2'] = simbolo_jogador2

def consulta_vitoria(tabuleiro):
    simbolo_jogador1 = session.get('simbolo_jogador1')
    simbolo_jogador2 = session.get('simbolo_jogador2')

    #Consulta todas as linhas do tabuleiro em busca de 3 valores iguais na mesma linha
    for linha in range(3):
        if tabuleiro [linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2]:
            if tabuleiro[linha][0] == simbolo_jogador1:
                    return 'jogador1'
            elif tabuleiro[linha][0] == simbolo_jogador2:
                return 'jogador2'
    #Consulta todas as colunas do tabuleiro em busca de 3 valores iguais na mesma coluna
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] ==tabuleiro[2][coluna]:
            if tabuleiro[0][coluna] == simbolo_jogador1:
                return 'jogador1'
            elif tabuleiro[0][coluna] == simbolo_jogador2:
                return 'jogador2'
                    
    #Consulta as duas diagonais di tabuleiro em busca de 3 valores iguais na mesma diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        if tabuleiro[1][1] == simbolo_jogador1:
            return 'jogador1'
        elif  tabuleiro[1][1] == simbolo_jogador2:
            return 'jogador2'
        
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        if tabuleiro[1][1] == simbolo_jogador1:
            return 'jogador1'
        elif tabuleiro[1][1] == simbolo_jogador2:
            return 'jogador2'
        
    return None

#Consulta se o jogo terminou e não ouve ganhador
def consultar_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula != "X" and celula != "O":
                return False
    return True

#Função que realiza as jogadas
def jogada(tabuleiro, posicao, simbolo_jogador):    
    linha = (posicao - 1) // 3
    coluna = (posicao -1 ) % 3
    if tabuleiro[linha][coluna] != "X" and tabuleiro[linha][coluna] != "O":
        tabuleiro[linha][coluna] = simbolo_jogador
        return True
    return False

                  