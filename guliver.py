def prime_number(n):
    if n == 2:
        return 2

    for p in range(2, n**(1/2)+1):
        if n%p==0:
            return
      
    return n

lisa = [3,7, 89, 44, 66, 2002, 19958766563245687]

for i in lisa:
    print(prime_number(i))