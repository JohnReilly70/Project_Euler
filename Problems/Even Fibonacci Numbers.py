def fibonaccia(n):

    if n <= 1:
        return n
    else:
        return fibonaccia(n-1) + fibonaccia(n-2)

def fibonaccia_yield():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def fibonaccia_yield_sum_even(n,less_than_value):
    f = fibonaccia_yield()
    sum_value =0
    counter = 0
    for value in f:
        if value % 2 == 0 and value < less_than_value:
            sum_value += value
        counter += 1
        if counter > n:
            break
    return sum_value


print(fibonaccia_yield_sum_even(100, 14000000))



