# Define a recursive function to generate Fibonacci numbers
def fibonacci(n):
    # Base condition: if n is 0 or 1, return n itself
    if n <= 1:
        return n
    else:
        # Recursive case: sum of the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take input from user for how many terms to generate
terms = int(input("Enter a term: "))

# Loop through each term and print Fibonacci sequence
for i in range(terms):
    # Call fibonacci() function for each index and print value
    print(fibonacci(i), end=" ")
