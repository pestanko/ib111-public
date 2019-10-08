#! /usr/bin/env python

def is_prime(num: int) -> bool:
    if num < 0:
        num *= -1

    if num == 0:
        return False

    for i in range(1, num, 2):
        if num % i == 0:
            return False
    return True

def computeGCD(num1: int, num2: int) -> int:
    smaller = num2

    if num1 < num2: 
        small = num1
    
    for i in range(1, smaller+1): 
        if (num1 % i == 0) and (num2 % i == 0): 
            return i
              
def print_is_prime(num: int):
    result = "is a prime!" if is_prime(num) else "is not a prime!"
    print(f"-> Number {num}", result)


def numbers_stats(num1: int, num2: int):
    print(f"Statistics for numbers {num1} and {num2}:")
    print_is_prime(num1)
    print_is_prime(num2)
    print(f"-> GCD({num1}, {num2}) =", computeGCD(num1, num2))
    print("->", num1, "is", "greater" if num1 > num2 else "smaller", "than", num2)

if __name__ == '__main__':
    numbers_stats(5, 4)
    print()
    numbers_stats(131, 111)


