import random as rd

def jogar():
    palavras = ["goku", "naruto", "luffy", "ichigo", "sasuke", "gon", "vegeta", "deku", "erza", "itadori", "gojo", "zoro", "lelouch", "gintoki", "isagi", "kagome", "inuyasha", "megumi", "spike", "rem"]
    
    palavra_secreta = rd.choice(palavras).upper()
    letras_acertadas = ["_" for _ in palavra_secreta]
    
    imprime_mensagem_abertura()
    
    enforcou = False
    acertou = False
    erros = 0
    
    while not enforcou and not acertou:
        print("\n" + " ".join(letras_acertadas) + "\n")
        chute = pede_chute()
        
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if acertou:
        imprime_mensagem_vencedor(palavra_secreta)
        jogar_novamente()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        jogar_novamente()

def desenha_forca(erros):
    if erros == 0:
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\    ")
        print(" |            ")
        print(" |            ")
    elif erros == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|   ")
        print(" |            ")
        print(" |            ")
    elif erros == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |            ")
        print(" |            ")
    elif erros == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |       |    ")
        print(" |            ")
    elif erros == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |       |    ")
        print(" |      /     ")
    else:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |       |    ")
        print(" |      / \\  ")

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print(f"A palavra era {palavra_secreta}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == chute:
            letras_acertadas[i] = chute

def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def jogar_novamente():
        print("Deseja jogar novamente? \n (1) SIM \n (2) NÃO")
        resposta = input("Digite sua resposta: ")

        if resposta == "2":
            print("Obrigado por jogar")
        elif resposta == "1":
            jogar()
        else:
            print("Resposta inválida")
            jogar_novamente()


if __name__ == "__main__":
    jogar()