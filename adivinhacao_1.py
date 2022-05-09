print("***********************************")
print("Bem vindo ao jogo de adivinhação com laço for!")
print("***********************************")

numero_secreto = 37
total_de_tentativas = 3

#laço de repetição: enquanto ainda há tentativas
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or  chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
        #continuar com a interação

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou! =)")
        break
        #sair do laço
    else:
        if(maior):
            print("Você errou!:( Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou!:( Seu chute foi menor que o número secreto.")
    # incrementando
    rodada = rodada + 1
print("Fim do jogo.")