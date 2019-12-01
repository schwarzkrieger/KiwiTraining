"""Solutions of module 3"""
import math

def sum_of_digits(num):
    """Return sum of digits of an integer n."""
    num = abs(num)
    summ = 0
    while num > 0:
        summ += num%10
        num //= 10
    return summ

def to_digits(num):
    """Return a list of digits of an integer n"""
    num = abs(num)
    digits = []
    while num > 0:
        digits.append(num%10)
        num //= 10
    digits.reverse()
    return digits

def to_number(digits):
    """Return a number based on digits"""
    digits.reverse()
    num = 0
    for i, val in enumerate(digits):
        num += val * 10 ** i
    return num

def count_vowels(strng):
    """Return count ov vovels in a string"""
    vowels = 'aeiouy'
    num_vowels = 0
    for char in strng.lower():
        if char in vowels:
            num_vowels += 1
    return num_vowels

def count_consonants(strng):
    """Return count ov consonants in a string"""
    consonants = 'bcdfghjklmnpqrstvwxz'
    num_consonants = 0
    for char in strng.lower():
        if char in consonants:
            num_consonants += 1
    return num_consonants

def prime_number(num):
    """Return true if n is prime number"""
    if num == 2:
        return True
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def fact_digits(num):
    """Return the sum of factoriel of each digit of a numner"""
    sum_factorial = 0
    for digit in to_digits(num):
        sum_factorial += math.factorial(digit)
    return sum_factorial

def fibonacci(num):
    """Return num-th member of the Fobonacci sequence"""
    fibonacci_seq = [1, 1]
    for i in range(2, num + 1):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq[0:num]

def fib_number(num):
    """Return a string of Fibonacci sequence to num-th member"""
    fibonacci_str = "".join(map(str, fibonacci(num)))
    return int(fibonacci_str)

def palindrome(num):
    """Check if n is palindrome"""
    str_n = str(num).replace(" ", "")
    for i in range(len(str_n)//2):
        if str_n[i] != str_n[-i-1]:
            return False
    return True

def char_histogram(string):
    """Return a dictionary with number of occurrences of each character in string"""
    histogram = {}
    for char in string:
        histogram[char] = string.count(char)
    return histogram
