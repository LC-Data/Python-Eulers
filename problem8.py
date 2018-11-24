### THIS CAN BE REAFCTORED BEAUTIFULLY, perhaps return some point in the future to do that

def largestProduct(sequenceLength): 		#enter the number of digits in a row you want evaluated - in our case Project Euler wants 13 digits

	num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450;
	num2string = str(num);		#turn int in to string.

	exploded = list(num2string);	#turn string in to list of individial characters.

	start0 = 0;		#provide indeces to use as starting parameters for the loop below.
	finish = sequenceLength;

	allOfThem = []; #list for all possible 13-character sequences
		
	for x in range(0,len(exploded) - 12):			#leave out the last 13 elements from the list because we are taking 13 elements at a time -- we don't want to go out of bounds.
		allOfThem.append(exploded[start0:sequenceLength])	#populate list with all possible sequences
		start0 = start0 +1;
		sequenceLength = sequenceLength +1;


	withoutZeroes = [];	#Now that we have all of those combinations, we want a new list that excludes all of the values that have a 0 anywhere in them

	for x in allOfThem:			#If there is a 0 in one of the sequences we don't want to add it do this list because it will yield a product of 0
		if ('0' not in x):
			withoutZeroes.append(x);
			#print(str(x) + "\n");


	joined = [];		#now that we have all combinations sans 0s, we want to "implode" them by joining the characters in the lists, in the list "withoutZeroes"

	for number in withoutZeroes:
		condensed = ''.join(str(i) for i in number)
		joined.append(condensed);

	prods = [];		#now let's calculate the products of each of those entries

	for x in joined:
		z = list(str(x));
		numski = 1;
		for y in z:
			numski = numski*(int(y));
			prods.append(numski);	#and append them to that list

	print(max(prods));	#now we return the largest product!

largestProduct(13);
