import time

from typing import List

def time_measure(func) -> None:
    start = time.time()
    func()
    end = time.time()
    diff = end - start
    print(f"Func {func.__name__} takes {diff:.08f} sec")


def is_prime(number: int) -> bool:
    if number <= 1: 
        return False
    
    for i in range(2, number, 1):
        if number % i == 0:
            return False
    return True

def divisors_with_prime(number: int) -> List[int]:
    return [d for d in range(2, number) if (number % d == 0 and is_prime(d))]

def divisors_better(number: int) -> List[int]:
    divisors = []
    i = 2
    while number > 1:
        if number % i == 0:
           divisors.append(i)
        while number % i == 0:
            number //= i
        i += 1
    return divisors


def print_divisors_prime():
    number = 2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 7 * 73
    print(f"Divisors of {number} are {divisors_with_prime(number)}")


def print_divisors_better():
    number =  2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 7 * 73
    print(f"Divisors of {number} are {divisors_better(number)}")


def find_in_array():
    array = [*range(0, 100000, 2)]
    for i in array:
        if 98854 == i:
            print("found")
            return
    print("not found")

def binary_search(needle, haystack):
    lower_bound = 0
    upper_bound = len(haystack) - 1
    while lower_bound <= upper_bound:
        middle = int((lower_bound + upper_bound) / 2)
        if haystack[middle] == needle:
            return True
        elif haystack[middle] > needle:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return False

def bfind_in_array():
    array = [*range(0, 100000, 2)]
    if binary_search(98854, array):
        print("found")
    else:
        print("not found")
        
if __name__ == '__main__':
    time_measure(print_divisors_better)
    time_measure(print_divisors_prime)
    print("-------------")
    time_measure(bfind_in_array)
    time_measure(find_in_array)


