def primeSums(n):
    primes = [];

    def isPrime(n):

        if n < 2: return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        primes.append(n);

    for x in range(0,n + 1):
        isPrime(x);

    sum = 0;
    for y in primes:
        sum = sum + y;

    print(primes);
    print(sum);

primeSums(2000000);
