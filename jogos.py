import forca
import adivinhacao

while True:
    print('*' * 30)
    print(f'{"Qual jogo quer jogar?":^30}')
    print('*' * 30)

    print('[1] Forca [2] Adivinhação [3] Sair')
    jogo = int(input('Qual jogo deseja jogar? '))

    if jogo == 1:
        print('Jogo da Forca escolhido.')
        forca.jogar()

    elif jogo == 2:
        print('Jogo e Adivinhação escolhido.')
        adivinhacao.jogar()

    elif jogo == 3:
        print('Obrigado! Volte sempre.')
        break


