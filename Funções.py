def somaImposto(taxaImposto,custoAntes):
    taxaPorcentagem = (taxaImposto / 100) + 1
    return custoAntes * taxaPorcentagem


def tamanhoNum(numeroInt):
    x = 0
    numeroInt = abs(numeroInt)
    while (numeroInt != 0):
        numeroInt = numeroInt // 10
        x = x + 1
    return x


def ultimoDig(num):
    return num % 10


def acumulaSoma(soma,ultimoDigito,tamanhoNumero):
    return soma + (ultimoDigito * (10 ** (tamanhoNumero - 1)))


def DivisaoInteiraPor10(num):
    return num // 10


def TesteNeg(num):
    if num <= 0:
        return 0
    else:
        return num


def main():
    valor_cru = 1123
    impostoini = 300

    impostoini = TesteNeg(impostoini)
    num_invertido = 0
    valor = int(somaImposto(impostoini,valor_cru))
    print(valor)
    while (valor > 0):
        num_invertido = acumulaSoma(num_invertido,ultimoDig(valor),tamanhoNum(valor))
        valor = DivisaoInteiraPor10(valor)

    print(num_invertido)


if __name__ == "__main__":
    main()
