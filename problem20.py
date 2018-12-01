def factorialDigitSum(goal):

	factorial = 1;
	factorialSum = 0;

	for i in range (1, goal + 1):
		factorial = factorial * i;


	factorialList = list(str(factorial));


	for x in factorialList:
		factorialSum = int(x) + factorialSum;

	print(factorial);
	print(factorialSum);

factorialDigitSum(100);
