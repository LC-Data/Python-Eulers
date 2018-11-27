import sys
sys.setrecursionlimit(1250)

def master(n):
	topCount = [0];
	topNum = [0];

	def checker(n, count, thisPass):

		if (n == 1):
			#print("We are done.")
			#print(str(count) + " number of nodes in " + str(thisPass));

			if (count > topCount[0]):
				topCount[0] = count;
				topNum[0] = thisPass;

		elif (n % 2 == 0):
			even(n, count, thisPass);
		elif (n % 2 != 0):
			odd(n, count, thisPass);

	def even(n, count, thisPass):
		n = n/2;
		count = count + 1;
		checker(n, count, thisPass);

	def odd(n, count, thisPass):
		n = (3*n + 1);
		count = count + 1;
		checker(n, count, thisPass);

	for i in range(1, n + 1):
		checker(i, 0, i);

	print(topCount, topNum)

master(999999)
