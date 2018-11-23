def sumOfMults(under):

	multiples = [];
	total = 0;
	for i in range (1, under):
		if (i % 3 == 0 or i % 5 == 0):
			multiples.append(i);

	for x in multiples:
		total = total + x;

	print(total);

sumOfMults(1000);
