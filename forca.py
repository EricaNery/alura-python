def jogar(): #função definida
    #todo o código identado faz parte da função

    print("*******************************")
    print("***Jogo de Forca - Estático****")
    print("*******************************")

    #declaração de variáveis
    palavra_secreta = "banana" #estático
    letras_acertadas = ["_", "_", "_", "_","_", "_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)

    #enquanto (True)
    #enquanto (True e True)
    #enquanto (não False e não False)
    #enquanto (não enforcou e não acertou)
    while(not enforcou and not acertou): #laço while

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:  #para letra em palavra_secreta
            if (chute.upper()  == letra.upper()): # se chute  for igual a letra.
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()