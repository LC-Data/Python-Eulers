def problem7():
	
	primes = [0];
	prime = [0];

	def is_prime(n):
	    """"pre-condition: n is a nonnegative integer
	    post-condition: return True if n is prime and False otherwise."""
	    if n < 2: 
	         return False;
	    if (n == 2):
	    	primes[0] = primes[0] + 1;
	    	prime[0] = n;
	    	print(prime[0], " is the ", primes[0], "-th prime.")
	    if n % 2 == 0:             
	         return n == 2  # return False
	    k = 3
	    while k*k <= n:
	         if n % k == 0:
	             return False
	         k += 2

	    primes[0] = primes[0] + 1;
	    prime[0] = n;
	    print(prime[0], " is the ", primes[0], "-th prime.")


	k = 1;
	while (primes[0] < 10001):
		is_prime(k);
		k = k + 1;

	print(primes);
	print(prime[0], " is the 10,001st prime.")

problem7();
