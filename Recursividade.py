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


def somartodosnumeros(num):
    if num == 0:
        return 0
    else:
        return num + (somartodosnumeros(num - 1))


def calculcarpot(base,expo):
    if expo == 0:
        return 1
    else:
        return base * (calculcarpot(base,expo - 1))


def numerodedigitos(num):
    if num == 0:
        return 0
    else:
        x = 1
        return x + (numerodedigitos(num // 10))


def mdc(a,b):
    if a == 0 and b == 0:
        return
    else:
        return mdc(b,a % b)


# def inverteStr(string):

# def Find(arr,x,seta):
#    if x!=arr(seta):
#       seta = seta + 1

contem = 'tem o numero'
naocontem = 'nao contem o numero'


# A = [1,3,4,6,3,6]
# cont = len(A) - 1
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
        return find3(tiraprimeiroitem(array),num)
    else:
        array[0] = 'nao'
        return naocontem


def tiraprimeiroitem(lista):
    for i in range(len(lista) - 1):
        lista[i] = lista[i + 1]
        lista[i + 1] = 'end'
    return lista


def main():
    n1 = 7
    a = [10,4,3,67,3,5,23,72]

    print(find3(a,n1))
    # print(find(array,40, seta))
    # print(Fibonacci(n1))
    # print(Fatorial(n1))
    # print(somarTodosNumeros(n1))
    # print(calculcarPot(n1,n1))
    # print(numeroDeDigitos(n1))
    # print(mdc(n1,n2))


if __name__ == "__main__":
    main()
