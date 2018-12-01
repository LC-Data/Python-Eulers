def fib():

	fibs = [];
	first = 0;
	second = 1;

	fibs.append(len(str(first)));
	fibs.append(len(str(second)));

	newNum = first + second;

	newNum2str = str(newNum);

	listNum = list(newNum2str);

	lenNum = len(listNum);

	while (lenNum < 1000):
		
		first = second;
		second = newNum;

		newNum = first + second;

		newNum2str = str(newNum);

		listNum = list(newNum2str);

		lenNum = len(listNum);

		fibs.append(lenNum);

		print("The index of the list is: ", (len(fibs)));

fib();
