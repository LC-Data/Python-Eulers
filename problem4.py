def largePalindromes():

	palindromes = [];

	for x in range(100,1000):
		for z in range(100,1000):
			num = x * z;
			if str(num) == str(num)[::-1]:
				palindromes.append(num);

	print max(palindromes);

largePalindromes();
