def jogar():
    from random import randint

    print('*' * 30)
    print(f'{"Adivinhe o núemro secreto":^30}')
    print('*' * 30)

    numero_secreto = randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print('Nível de dificuldade: [1] Fácil [2] Médio [3] Difícil')
    nivel = int(input('Qual nível de dificuldade deseja? '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = input('Digite seu número entre 1 e 100: ')
        print(f'Você digitou {chute_str}.', end=' ')
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print('Você deve digitar o núemro entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if chute == numero_secreto:
            print(f'Você acertou! e fez {pontos} pontos!')
            break
        else:
            if chute > numero_secreto:
                print('Você errou! O seu chute foi maior do que o número secreto')
            elif chute < numero_secreto:
                print('Você errou! Seu chute foi menor do que o núemro secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print('Fim do jogo!')

if __name__ == "__main__":
    jogar()