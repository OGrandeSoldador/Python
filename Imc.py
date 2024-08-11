print('Qual seu IMC?')
while 0 == 0:
    altura = float(input('Qual sua altura?(em Cm)'))
    peso = float(input('Qual seu Peso?(em Kg))'))
    imc = peso / (altura ** 2)
    imc = (10 ** 4) * imc
    print(f'Seu IMC é: {imc:.1f}')
