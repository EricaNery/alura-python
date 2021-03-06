import random

def jogar():
    # todo o código identado faz parte da função
    print("*******************************")
    print("Jogo de adivinhação com níveis!")
    print("*******************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #laço de repetição: enquanto ainda há tentativas
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or  chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue   #continuar com a interação

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou! =) e fez {} pontos!" .format(pontos))
            break  #sair do laço
        else:
            if(maior):
                print("Você errou!:( Seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou!:( Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #40-20=20
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1  # incrementando

    print("Fim do jogo.")

if(__name__ == "__main__"):
    jogar()