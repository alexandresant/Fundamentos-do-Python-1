tabuleiro = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]

def jogada_jogador(tabuleiro):
  fim_jogada = False
  while not fim_jogada:
    jogada = input("Digite um número: ")

    for linha in tabuleiro:
      for j in range(len(linha)):
        if linha[j] == jogada:
          linha[j] = "O"
          fim_jogada = True
    if not fim_jogada:
          print("Jogada inválida")

def jogada_computador(tabuleiro):
  fim_jogada = False
  while not fim_jogada:
    computador = randrange(1, 10)
    for linha in tabuleiro:
      for j in range(len(linha)):
        if linha[j] == str(computador):
          linha[j] = "X"
          fim_jogada = True

def imprime_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print("+-------" * 3, end="+\n")
    print("|       " * 3, end="|\n")
    for col in linha:
      print("|   " + col + "   ", end="")
    print("|\n")
    print("|       " * 3, end="|\n")
  print("+-------" * 3, end="+\n")

def verifica_fim_jogo(tabuleiro, jogador):
  for linha in tabuleiro:
    if all(item == jogador for item in linha):
        return True
  for coluna in range(3):
    if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
      return True

  if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
    return True
  if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0]  == jogador:
    return True
  if len(criar_lista_casas_livres(tabuleiro)) == 0:
    print("Deu Velha!")
    return True

  return False

def criar_lista_casas_livres(tabuleiro):
  campos_livres = []
  for linha in range(3):
    for coluna in range(3):
      if tabuleiro[linha][coluna] not in ["X", "O"]:
        campos_livres.append((linha, coluna))
  return campos_livres

fim_jogo = False
imprime_tabuleiro(tabuleiro)

while not fim_jogo:
  jogada_jogador(tabuleiro)

  imprime_tabuleiro(tabuleiro)

  if verifica_fim_jogo(tabuleiro,"O"):
    print("Jogador Venceu!!!")
    fim_jogo = True

  if verifica_fim_jogo(tabuleiro,"X"):
    print("Computador Venceu!!!")
    fim_jogo = True

  jogada_computador(tabuleiro)

  if verifica_fim_jogo(tabuleiro,"O"):
    print("Jogador Venceu!!!")
    fim_jogo = True

  if verifica_fim_jogo(tabuleiro,"X"):
    print("Computador Venceu!!!")
    fim_jogo = True

  imprime_tabuleiro(tabuleiro)