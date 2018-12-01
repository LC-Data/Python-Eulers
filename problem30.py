def sumFifths():	
	total = 0;


	for i in range (1, 5000001):
		sum = 0;
		number2string = str(i);
		for x in range(0,len(number2string)):
			sum = sum + (int(number2string[x])**5);

		if (int(sum) == int(i)):
			print('WE DID IT!', i);
			total = total + i;
			print("The final total was ", total - 1);

sumFifths();
