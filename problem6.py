def difference(top):

	sum = 0;
	square = 0;

	for i in range (1, top + 1):
		sum = sum + (i*i);
	print(sum);

	for x in range (1, top + 1):
		square = square + x;

	square = square*square;
	print(square);

	difference = square - sum;

	print(difference);

difference(100);
