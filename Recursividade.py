# Função
def fibonacci(num):
    if num < 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fatoria(num):
    if num == 0:
        return 1
    else:
        return num * (fatoria(num - 1))


def somarTodosNumeros(num):
    if num == 0:
        return 0
    else:
        return num + (somarTodosNumeros(num - 1))


def calculcarPot(base,expo):
    if expo == 0:
        return 1
    else:
        return base * (calculcarPot(base,expo - 1))


def numeroDeDigitos(num):
    if num == 0:
        return 0
    else:
        x = 1
        return x + (numeroDeDigitos(num // 10))


def mdc(a,b):
    if a == 0 and b == 0:
        return
    else:
        return mdc(b,a % b)


#def inverteStr(string):

#def Find(arr,x,seta):
#    if x!=arr(seta):
#       seta = seta + 1

contem = 'tem o numero'
naocontem = 'nao contem o numero'


#A = [1,3,4,6,3,6]
#cont = len(A) - 1
def find(array,num):
    global cont
    if cont < 0:
        return naocontem
    if array[cont] == num:
        return contem
    else:
        cont -= 1
        return find(array,num)


def find2(array,num,x):
    if array[x] != num:
        x = x + 1
        return find2ax(array,num,x)
    else:
        return contem


def find2ax(array,num,x):
    if x != len(array):
        return find2(array,num,x)
    else:
        return naocontem


def find3(array,num):
    if array[0] == num:
        return contem
    if array[0] != 'end':
        return find3(tiraPrimeiroItem(array),num)
    else:
        array[0] = 'nao'
        return naocontem


def tiraPrimeiroItem(list):
    global i
    for i in range(len(list) - 1):
        list[i] = list[i + 1]
    list[i + 1] = 'end'
    return list


def main():
    n1 = 4
    n2 = 3
    A = [10,4,3,67,3,5,23,72]
    zero = 0

    print(find3(A,72))
    print(tiraPrimeiroItem(A))
    #print(find(array,40, seta))

    #print(Fibonacci(n1))
    #print(Fatorial(n1))
    #print(somarTodosNumeros(n1))
    #print(calculcarPot(n1,n2))
    #print(numeroDeDigitos(n1))
    #print(mdc(n1,n2))


if __name__ == "__main__":
    main()
