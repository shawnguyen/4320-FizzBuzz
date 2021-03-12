for i in range(1,101):
    #If number is a multiple of 3 and 5
    if i % 15 == 0:
        print ("FizzBuzz")
    #If number is a multiple of 3
    elif i % 3 == 0:
        print ("Fizz")
    #If number is a multiple of 5
    elif i % 5 == 0:
        print ("Buzz")
    #Print number if number is not a multiple of 3, 5, or both.
    else:
        print (str(i))
