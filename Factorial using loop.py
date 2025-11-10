num=int(input("Enter a number:"))
factorial=1        # if initialize with zero then everything will make zero

if num < 0:
    print("Factorial does not exist for negative numbers:")
elif num==0:
    print("The factorial of 0 is 1:")
else:
    for i in range(1,num+1):          # use num + 1 because range() stops one before the end.
        factorial=factorial*i
    print(f"The factorial of {num} is {factorial}")