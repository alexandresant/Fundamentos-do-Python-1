from flask import Blueprint, render_template, request, redirect, url_for, session
from app.game_logic import inicializar_tabuleiro, nomes_jogadores, consulta_vitoria, consultar_empate, jogada

#Definindo o Blueprint para as rotas
app_routes = Blueprint('app_routes', __name__)

#Rota para a página inicial
@app_routes.route('/')
def home():
    tabuleiro = session.get('tabuleiro', None)
    if not tabuleiro:
        tabuleiro = inicializar_tabuleiro()
        session['tabuleiro'] = tabuleiro
    return render_template('index.html', tabuleiro=tabuleiro)

#Rota para iniciar o jogo
@app_routes.route('/iniciar', methods=['POST'])
def iniciar_jogo():
    #coletar dados do formulario

    jogador1 = request.form['jogador1']
    jogador2 = request.form['jogador2']
    simbolo_jogador1 = request.form['simbolo']
    simbolo_jogador2 = 'X' if simbolo_jogador1 == 'O' else 'O'

    #Salvar as informações dos jogadores na seção
    nomes_jogadores(jogador1, jogador2, simbolo_jogador1, simbolo_jogador2)

    #Passar o tabuleiro para o template
    tabuleiro = inicializar_tabuleiro()
    session['tabuleiro'] = tabuleiro

    return render_template('index.html', tabuleiro=tabuleiro)

#Rota que irá processar a jogada verificar a posição escolhida e atualizar o tabuleiro
@app_routes.route('/jogada', methods=['POST'])
def realizar_jogada():
    posicao = int(request.form['posicao'])
    jogador = session.get('jogador1') if posicao % 2 == 1 else session.get('jogador2')
    simbolo_jogador = session.get('simbolo_jogador1') if jogador == session.get('jogador1') else session.get('simbolo_jogador2')

    #Processar a jogada
    tabuleiro = session.get('tabuleiro')
    if jogada(tabuleiro, posicao, simbolo_jogador):
        session['tabuleiro'] = tabuleiro
        vitoria = consulta_vitoria(tabuleiro)
        empate = consultar_empate(tabuleiro)

        if vitoria:
            return f'{vitoria} venceu'
        elif empate:
            return 'Empate!'
        else:
            return render_template('index.html', tabuleiro=tabuleiro)
    
    return redirect(url_for('app_routes.home'))

#Rota responsável por encerrar o jogo
@app_routes.route('/encerrar')
def encerrar_jogo():
    session.clear()
    return redirect(url_for('app_routes.home'))
