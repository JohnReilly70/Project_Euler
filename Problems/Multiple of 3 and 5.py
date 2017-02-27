def multiples_3_5(n):
    for number in range(1,n):
        if number % 3 == 0 or number % 5 == 0:
            yield number

print(sum(multiples_3_5(1000)))