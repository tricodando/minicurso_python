"""
    Lab (Sequência de Fibonacci)

    Problema: Criar uma função recursiva que retorna
    a sequência de fibonacci.

    fibonacci = 1, 1, 2, 3, 5, 8, ...
"""
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

termo = int(input("Digite o termo a ser buscado: "))
print(fib(termo))










"""
fib(5) =
    fib(4)
        fib(3)
            fib(2)
                fib(1) = 1
                fib(0) = 0
            fib(1) = 1
        fib(2)
            fib(1) = 1
            fib(0) = 0
    fib(3)
        fib(2)
            fib(1) = 1
            fib(0) = 0
        fib(1) = 1
"""
