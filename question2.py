def fib(first, second, total):

    if (second % 2 == 0):
        total = total + second;
        print("Total is now " + str(total) + " second was " + str(second));
    
    newNum = first + second;
    if (newNum > 4000000):
        print("WE DID IT! The final sum is: ", total);
    else:
        fib(second, newNum, total);

fib(1,2,0);
