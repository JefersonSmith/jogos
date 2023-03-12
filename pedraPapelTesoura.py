import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Pedra, Papel e Tesoura!")
    print("*********************************")

    jogar_novamente = "sim"

    while (jogar_novamente == "sim"):
        jogador = int(input('''Escolha uma opção:
         [0] Pedra
         [1] Papel
         [2] Tesoura
         Digite sua escolha: '''))

        computador = random.randint(0, 2)

        if(computador == 0):
            print("computador escolhe pedra")
            if(jogador == 0):
                print("Empate!")
            elif(jogador == 1):
                print("Jogador Venceu")
            elif(jogador == 2):
                print("Jogador perdeu")


        elif(computador == 1):
            print("computador escolheu papel")
            if(jogador == 0):
                print("Jogador Perdeu!")
            elif(jogador == 1):
                print("Empate")
            elif(jogador == 2):
                print("Jogador venceu")


        elif(computador == 2):
            print("computador escolheu tesoura")
            if(jogador == 0):
                print("Jogador Venceu!")
            elif(jogador == 1):
                print("Jogador Perdeu")
            elif(jogador == 2):
                print("Empate")

        jogar_novamente = input("Você quer tentar novamente? Digite sim ou não: " )
    print("Até a próxima!" )

if(__name__ == "__main__"):
    jogar()
