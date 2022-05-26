def jogar(): #função definida
    #todo o código identado faz parte da função

    print("*******************************")
    print("***Jogo de Forca - Estático****")
    print("*******************************")

    #declaração de variáveis
    palavra_secreta = "maça" #estático

    enforcou = False
    acertou = False

    #enquanto (True)
    #enquanto (True e True)
    #enquanto (não False e não False)
    #enquanto (não enforcou e não acertou)
    while(not enforcou and not acertou): #laço while

        chute = input("Qual letra?")
        index = 0
        for letra in palavra_secreta:  #para letra em palavra_secreta
            if (chute  == letra): # se chute  for igua letra)
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("jogando...")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()