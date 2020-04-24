#  -*- coding: utf-8 -*-
class JogoDaVelha():


    def __init__(self, tabuleiro, jogador):
        self._jogador = jogador
        self._tabuleiro = tabuleiro

    def definirTabuleiro(self):
        self._tabuleiro = {'EC': 'EC', 'MC': 'MC', 'DC':  'DC', 'EM': 'EM', 'MM': 'MM', 'DM': 'DM', 'EB': 'EB', 'MB': 'MB', 'DB': 'DB'}
        self._jogador = 1

    def mostrarTabuleiro(self):
        print(self._tabuleiro['EC'] + '  |  ' + self._tabuleiro['MC'] + '  | ' + self._tabuleiro['DC'])
        print('---+-----+-----')
        print(self._tabuleiro['EM'] + '  |  ' + self._tabuleiro['MM'] + '  | ' + self._tabuleiro['DM'])
        print('---+-----+-----')
        print(self._tabuleiro['EB'] + '  |  ' + self._tabuleiro['MB'] + '  | ' + self._tabuleiro['DB'])

    def ganhador(self):
        if self._tabuleiro.get('EC')==self._tabuleiro.get('MC') and self._tabuleiro.get('MC')==self._tabuleiro.get('DC') or \
            self._tabuleiro.get('EC')==self._tabuleiro.get('EM') and self._tabuleiro.get('EM')==self._tabuleiro.get('EB') or \
            self._tabuleiro.get('EC')==self._tabuleiro.get('MM') and self._tabuleiro.get('MM')==self._tabuleiro.get('DB'):
            if self._tabuleiro.get('EC')=='X':
                print('Jogador 1, ',self._tabuleiro.get('EC'),', ganhou!')
            else:
                print('Jogador 2, ',self._tabuleiro.get('EC'),', ganhou!')
            return True
        elif self._tabuleiro.get('EM')==self._tabuleiro.get('MM') and self._tabuleiro.get('MM')==self._tabuleiro.get('DM') or \
            self._tabuleiro.get('MC')==self._tabuleiro.get('MM') and self._tabuleiro.get('MM')==self._tabuleiro.get('MB'):
            if self._tabuleiro.get('MM')=='X':
                print('Jogador 1, ',self._tabuleiro.get('EM'),', ganhou!')
            else:
                print('Jogador 2, ',self._tabuleiro.get('EM'),', ganhou!')
            return True
        elif self._tabuleiro.get('EB')==self._tabuleiro.get('MB') and self._tabuleiro.get('MB')==self._tabuleiro.get('DB') or \
            self._tabuleiro.get('EB')==self._tabuleiro.get('MM') and self._tabuleiro.get('MM')==self._tabuleiro.get('DC'):
            if self._tabuleiro.get('EB')=='X':
                print('Jogador 1, ',self._tabuleiro.get('EB'),', ganhou!')
            else:
                print('Jogador 2, ',self._tabuleiro.get('EB'),', ganhou!')
            return True
        elif self._tabuleiro.get('DC')==self._tabuleiro.get('DM') and self._tabuleiro.get('DM')==self._tabuleiro.get('DB'):
            if self._tabuleiro.get('DC')=='X':
                print('Jogador 1, ',self._tabuleiro.get('DC'),', ganhou!')
            else:
                print('Jogador 2, ',self._tabuleiro.get('DC'),', ganhou!')
            return True
        else:
            return False

    def alterarTabuleiro(self, x):

        if self._jogador==1 and x!=9:
            pos1 = str(input('Jogador 1, X, escolha uma posição: '))
            pos1 = pos1.upper()
            valor = self._tabuleiro.get(pos1)
            try:
                if valor.strip()==pos1.strip():
                    self._tabuleiro[pos1] = ' '
                    self._tabuleiro[pos1] = 'X'
            except Exception:
                print('Posição inválida!')
                x -= 1

            jv.mostrarTabuleiro()
            jv.ganhador()
            self._jogador = 2

        else:
            self._jogador=1
            pos2 = str(input('Jogador 2, O, escolha uma posição: '))
            pos2 = pos2.upper()
            valor = self._tabuleiro.get(pos2)
            try:
                if valor.strip()==pos2:
                    self._tabuleiro[pos2] = ' '
                    self._tabuleiro[pos2] = 'O'
            except Exception:
                print('Posição inválida!')
                x -= 1

            jv.mostrarTabuleiro()
            jv.ganhador()


jv = JogoDaVelha('',0)
jv.definirTabuleiro()
jv.mostrarTabuleiro()
for x in range(9):
    if jv.ganhador() is False:
        jv.alterarTabuleiro(x)
        if x==8:
            print('Deu velha!')
    else:
        x=9
