def powerDigits(num, exp):

	finalNum = list(str(num ** exp));
	print(finalNum);

	sumOfDigits = 0;

	for x in finalNum:
		sumOfDigits = sumOfDigits + int(x);
		print("Sum of the digits is now at, " + str(sumOfDigits));

powerDigits(2,1000);
