def fib(n):
    def tailFib(counter, a, b):
        if counter == 0:
            return a
        elif counter == 1:
            return b
        else:
            return(tailFib(counter-1, b, a+b))
    return tailFib(n, 1, 1)

print(fib(9))
