def somaImposto(taxaImposto,custoAntes):
    taxaPorcentagem = (taxaImposto/100)+1
    return custoAntes*taxaPorcentagem

def tamanhoNum(numeroInt):
    x=0
    numeroInt = abs(numeroInt)
    while (numeroInt!=0):
         numeroInt = numeroInt//10
         x = x+1
    return x

def ultimoDig(num):
    return num % 10

def acumulaSoma(soma,ultimoDigito,tamanhoNumero):
    return soma + (ultimoDigito*(10**(tamanhoNumero-1)))

def DivisaoInteiraPor10(num):
    return num//10

def TesteNeg(num):
    if num<=0:
        return 0
    else:
        return num

def main():

    ValorCru= 1123
    ImpostoIni= 300

    ImpostoIni = TesteNeg(ImpostoIni)
    numInvertido=0
    Valor = int(somaImposto(ImpostoIni,ValorCru))
    print(Valor)
    while(Valor>0):
        numInvertido = acumulaSoma(numInvertido, ultimoDig(Valor), tamanhoNum(Valor))
        Valor = DivisaoInteiraPor10(Valor)

    print(numInvertido)

if __name__ == "__main__":
        main()





