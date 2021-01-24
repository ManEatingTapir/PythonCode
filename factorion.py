def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return factorial(number - 1) * number

# Takes about 10 seconds
def factorion():
    # Original task was to check all numbers from 1 to ten million, lowered the upper bound through some logic and math
    # actual upper bound is 40585 (last factorion)
    # bound I found was 1854722
    for integer in range(11, 1854722):
        # create counter variable
        sum = 0
        # map applies argument 1 (function) to every item of argument two (iterable)
        # in this case: str(integer) turns the integer into a string so I can loop through
        # and get each digit in the integer. But now that's a string
        # So then I have to turn it back into an integer, hence the int function.
        for c in map(int, str(integer)):
            # Add the factorial of each digit to the counter
            sum = sum + factorial(c)
        if sum == integer:
            print(sum)

if __name__ == '__main__':
    factorion()
    # Output: 145, 40585
