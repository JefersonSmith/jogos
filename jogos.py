import forca
import adivinhacao
import pedraPapelTesoura


def escolha_jogo():
    print("*********************************")
    print("Escolhe o seu jogo!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Pedra, Papel, Tesoura")

    jogo = int(input("Qual jogo?: "))

    if(jogo ==1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print ("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo ==3):
        print ("Jogando pedra, papel, tesoura")
        pedraPapelTesoura.jogar()

if(__name__ == "__main__"):
    escolha_jogo()