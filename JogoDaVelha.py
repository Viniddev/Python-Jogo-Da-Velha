# Agora sim, jogo da velha (modificado by me)
import os
import math
import random

jogarnovamente = "s"
jogadas = 0
quemjoga = 2  # 1= jogador1, 2=jogador2
maxjogadas = 9
vit = "n"
velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# --------------------------------------------------------------------------


def tela():
    global velha
    global jogadas
    os.system("cls")
    print(" "*19, "\033[1;31mJogo da Velha! Bora jogar?\033[m")
    print("\033[1;31m~\033[m"*67)
    print()
    print(" "*22, "    0    1    2")
    print(" "*22, "0:  " + velha[0][0] +
          "  | " + velha[0][1] + " | "+velha[0][2])
    print(" "*22, "   ------------")
    print(" "*22, "1:  " + velha[1][0] +
          "  | " + velha[1][1] + " | "+velha[1][2])
    print(" "*22, "   ------------")
    print(" "*22, "2:  " + velha[2][0] +
          "  | " + velha[2][1] + " | "+velha[2][2])
    print()
    print("jogadas: \033[1;31m" + str(jogadas), "\033[m")


tela()
# --------------------------------------------------------------------------


def jogadorJoga():
    global jogadas
    global quemjoga
    global maxjogadas
    if quemjoga == 2 and jogadas < maxjogadas:
        l = int(input('Qual a linha?: '))
        c = int(input('Qual a coluna?: '))
        try:
            while velha[l][c] != " ":
                l = int(input("Qual a linha? "))
                c = int(input("Qual a coluna? "))
            velha[l][c] = "X"
            quemjoga = 1
            jogadas += 1
        except:
            print("Linha e/ou coluna Invalida! tente novamente.")
            # vit="nao"
# -----------------------------------------------------------------------


def jogadordoisJoga():
    global jogadas
    global quemjoga
    global maxjogadas
    if quemjoga == 1 and jogadas < maxjogadas:
        l = int(input('Qual a linha?: '))
        c = int(input('Qual a coluna?: '))
        try:
            while velha[l][c] != " ":
                l = int(input("Qual a linha? "))
                c = int(input("Qual a coluna? "))
            velha[l][c] = "O"
            quemjoga = 2
            jogadas += 1
        except:
            print("Linha e/ou coluna Invalida! tente novamente.")
            # vit="nao"
# -------------------------------------------------------------------------


def verificarvitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # testar linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if(vitoria != "n"):
            break
        # verificar colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if(vitoria != "n"):
            break
        # verificar diagonal secundaria
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if(velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
        # verificar diagonal principal
        soma = 0
        idiagl = 0
        idiagc = 0
        while idiagl <= 2 and idiagl <= 2:
            if(velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc += 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria

# -----------------------------------------------------------------------


def redefinir():
    global velha
    global vit
    global quemjoga
    global maxjogadas
    global jogadas
    jogadas = 0
    quemjoga = 2  # 1= cpu, 2=jogador
    maxjogadas = 9
    vit = "n"
    velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# -----------------------------------------------------------------------


while jogarnovamente == "s":
    while True:
        tela()
        print(""*10, "\033[1;31mJogador X  joga\033[m", ""*10)
        jogadorJoga()
        tela()
        print(""*10, "\033[1;34mJogador O joga\033[m", ""*10)
        jogadordoisJoga()
        tela()
        vit = verificarvitoria()
        if vit != "n" or jogadas >= maxjogadas:
            break
    print("\033[1;31m Jogo encerrado! \033[m")
    if vit == "X" or vit == "O":
        print("Resultado: Jogador: " + vit + " Venceu!")
    else:
        print("Resultado: Empate!!! Tente novamente.")
    print()
    jogarnovamente = str(
        input("\033[1;34mDeseja jogar novamente?[s/n] \033[m"))
    jogarnovamente = jogarnovamente.lower()
    redefinir()
