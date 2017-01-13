""" Calculates the sum of the odd numbers from the Fibonacci sequence up to a certain number.

Usage example:
	python fibonacci.py 15

Works with Python 2 and 3.
"""

import sys

def fibonacci(num):
    """Generates the Fibonacci sequence up to num."""
    if num <= 0:
        raise ValueError('num should be > 0.')

    previous_two_nums = (1,1)
    #Yielding the first two ones
    for one in previous_two_nums:
    	yield one
    #Yielding all of the following numbers
    while sum(previous_two_nums) <= num:
        next_num = sum(previous_two_nums)
        previous_two_nums = (previous_two_nums[1], next_num)
        yield next_num

def is_odd(num):
    return num%2 == 1

def sum_odd_fibonacci_up_to_num(num):
    """Calculates the sum of the odd numbers of the Fibonacci sequence up to num."""
    fibonacci_up_to_num = list(fibonacci(num))
    odd_fibonacci_up_to_num = [number for number in fibonacci_up_to_num if is_odd(number)]
    sum_odd_fibonacci = sum(odd_fibonacci_up_to_num)

    print('\nFibonacci sequence up to %s: %s' % (num, fibonacci_up_to_num))
    print('Odd numbers from the Fibonacci sequence up to %s: %s' % (num, odd_fibonacci_up_to_num))
    print('Sum of the odd numbers: %s\n' % sum_odd_fibonacci)

    return sum_odd_fibonacci

if __name__ == "__main__":
	sum_odd_fibonacci_up_to_num(int(sys.argv[1]))
