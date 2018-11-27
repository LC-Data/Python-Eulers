def firstTenDigs():
	
	numData = [];

	with open("numFile.txt", 'r') as f:
	    for line in f:
	       numData.append(float(line.rstrip()));

	sum = 0;
	for x in numData:
		sum = sum + int(x);

	sum2str = (str(sum));

	print(sum2str[0:10])

firstTenDigs();
