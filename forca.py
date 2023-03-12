
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]


    enforcou = False
    acertou = False

    print("Palavra secreta:", letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual Letra?")
        chute = chute.strip() #strip remove os espaços na resposta do usuário

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #upper deixa tudo maiúsculo, caso usuário use um ou outro
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

        print("jogando...")


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
