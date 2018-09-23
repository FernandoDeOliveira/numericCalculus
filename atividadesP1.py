from numpy import e
# import euler number
from sympy import *
# import trigonometric functions and differentials
import matplotlib.pyplot as plt


# import lib to plot graphics

def exp(x, n=1000):
    """
    work with dictionaries for factorial functions
    is more efficient if exist continuous recursions
    """
    dic_fat = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}

    def fat(n):
        if n in dic_fat.keys():
            return dic_fat[n]
        else:
            dic_fat[n] = n * fat(n - 1)
            return dic_fat[n]

    e_power_x = 0.0
    if x < 0:       # if x it's negative
        return exp(-x)**(-1)
    else:
        for i in range(n):
            e_power_x += ((x ** i) / fat(i))
        return e_power_x


def f_a(x):
    return 4 * cos(x) - (e ** (2 * x))


def f_b(x):
    return (x / 2) - tan(x)


def f_c(x):
    return 1 - x * log(x)


def f_d(x):
    return (2 ** x) - 3 * x


def f_e(x):
    return (x ** 3) + x - 1000


def metedo_bisseccao(a, b, erro, n_max_iteracao, funcao):
    """
    :param a: intervalo inf.
    :param b: intervalo sup.
    :param erro: erro de precisao
    :param n_max_iteracao: num. de voltas no loop
    :param funcao: funcao a ser calculada
    :return: valor aproximado
    """
    
    while n_max_iteracao != 0:
        m = (a + b) / 2
        

        if funcao(m) == 0 or abs((b - a) / 2) < erro:
           return m

        [a, b] = [m, b] if funcao(b) * funcao(m) < 0 else [a, m]  # val a,b it's update to a new interval
        n_max_iteracao -= 1

    return "O metodo falhou apos intercoes"


def metodo_falsa_posicao(a, b, erro, n_max_iteracao, funcao):
    """
    :param a: intervalo inf.
    :param b: intervalo sup.
    :param erro: precisão de erro
    :param n_max_iteracao: numero iterações na funçao
    :param funcao: f(x)
    :return: raiz
    """
    def x_barra():
        return b - (n * (b - a)) / (n - m)

    for i in range(n_max_iteracao):
        m, n = funcao(a), funcao(b)
        x = x_barra()
        
        if abs(x - b) < erro:
            return x

        if funcao(x) * funcao(b) < 0:
            a, m = b, n

        b, n = x, funcao(x)   
    return "metodo falhou apos {numero} tentativas".format(numero=n_max_iteracao)


def metodo_ponto_fixo(x0, error, n_max_iteracao, funcao):
    """
    Calculate the root of a function by the method of fixed point
    :param x0: initial value
    :param error: error of approximation
    :param n_max_iteracao: number max of iteration for calculus
    :param funcao: mathematical function it's passed
    :return: approximately the root of the equation and plot the graphic
    """
    while (n_max_iteracao != 0):
        c = funcao(x0)        
        if abs(c - x0) < error:            
            return 'the root of the equation its approximately {}'.format(c)
        
        x0 = c
        n_max_iteracao -= 1
    return 'method fail after interactions'


def metodo_NR(x0, err1, err2, n_max_iteracao, funcao):
    """
    Calculate the root of a function by the method of Newton-Raphson
    :param x0: initial value
    :param err1: first error of approximation
    :param err2: second error of approximation
    :param n_max_iteracao: number of iteration for calculos
    :param funcao: mathematical function
    :return: approximately the root of the equation and plot the graphic
    """
    x, y = symbols('x y')
    # cria variáveis x e y

    y = funcao(x)
    # torna a funcao recebida na forma de equação y = f(x)

    dx = diff(y)
    # dx = derivada de y em função de x

    while (n_max_iteracao != 0):
        if abs(funcao(x0)) < err1:
            return x0

        x1 = x0 - (funcao(x0) / dx.subs(x, x0))
        if abs(funcao(x1)) < err1 or abs(x1 - x0) < err2:            
            return x1
        x0 = x1
    return "method fail after interactions"


def metodo_secante(x0, x1, erro, n_max_iteracao, funcao):
    m, n = funcao(x0), funcao(x1)
    
    while (n_max_iteracao != 0):
        c = x1 - ((n * (x1 - x0)) / (n - m))
        if abs(c - x1) < erro:
            return c
        x0 = x1
        m = n
        x1 = c
        n = funcao(c)
        n_max_iteracao -= 1
    return "o método falhou após interções"




met = int(input("""
digite o numero do método:
1 - metodo da bissecção
2 - metodo da falsa posição
3 - metodo do ponto fixo
4 - metodo de NR
5 - metodo da secante

numero ="""))

if met == 1:
    print("metodo da bissecção:")
    funcao = str(input("digite a função:\n f(x)="))
    exec("f = lambda x: {}".format(funcao))
    """
    a variavel "funcao" recebe uma funcao matematica 
    em forma de string.
    a funcao "exec" transforma uma string e 
    executa essa string como se fosse parte do código
    """

    a = float(input("digite o valro inicial do intervalo"))
    b = float(input("digte o valor final do intervalo"))
    erro = float(input("digite o valor do erro de precição"))
    n_max_iteracao = int(input("digite o numero máximo de interações da função"))

    raiz = metedo_bisseccao(a=a,
                            b=b,
                            erro=erro,
                            n_max_iteracao=n_max_iteracao,
                            funcao=f)
    print(raiz)
if met == 2:
    print("metodo da falsa posição")
    funcao = str(input("digite a função:\n f(x)="))
    exec("f = lambda x: {}".format(funcao))
    a = float(input("digite valor inicial do intervalo"))
    b = float(input("digite valor final do intervalo"))
    erro = float(input("digite o erro de aproximação"))
    n_max_iteracao = int(input("digite o numero máximo de interações da função"))

    raiz = metodo_falsa_posicao(a=a,
                                b=b,
                                erro=erro,
                                n_max_iteracao=n_max_iteracao,
                                funcao=f)
    print(raiz)
if met == 3:
    print("metodo do ponto fixo")
    funcao = str(input("digite a função:\n f(x)="))
    exec("f = lambda: x {}".format(funcao))
    x0 = float(input("digite valor do X0"))
    erro = float(input("digite o erro de aproximação"))
    n_max_iteracao = int(input("digite o numero máximo de interações"))

    raiz = metodo_ponto_fixo(x0=x0,
                             error=erro,
                             n_max_iteracao=n_max_iteracao,
                             funcao=f)
    print(raiz)
if met == 4:
    print("metodo NR")
    funcao = str(input("digite a função:\n f(x)="))
    exec("f = lambda x: {}".format(funcao))
    x0 = float(input("digite o valor de X0"))
    err1 = float(input("digite o valor do erro 1"))
    err2 = float(input("digite o valor do erro 2"))
    n_max_iteracao = "digite o numero máximo de iterações"

    raiz = metodo_NR(x0=x0,
                     err1=err1,
                     err2=err2,
                     n_max_iteracao=n_max_iteracao,
                     funcao=f)
    print(raiz)
if met == 5:
    print("metodo da secante")
    funcao = str(input("digite a função:\n f(x)="))
    exec("f = lambda x: {}".format(funcao))
    x0 = float(input("digite o valor de X0"))
    x1 = float(input("digite o valor de X1"))
    erro = float(input("digite o valor de erro de aproximação"))
    n_max_iteracao = int(input("digite o numero máximo de interações"))

    raiz = metodo_secante(x0=x0,
                          x1=x1,
                          erro=erro,
                          n_max_iteracao=n_max_iteracao,
                          funcao=f)
    print(raiz)

x = int(input("digite o valor de x para calucar exponencial\nx = "))
print("""
na função f(x) = e^x
f({x}) = {exp}
""".format(x=x, exp=exp(x)))
