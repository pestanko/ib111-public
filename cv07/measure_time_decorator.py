import time
import functools
from typing import List

ARRAY = [*range(0, 1000000, 2)]
NUMBER = 942185


def time_measure(func):
  @functools.wraps(func)
  def _wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    diff = end - start
    print(f"Decorator: Func {func.__name__} takes {diff:.08f} sec")
    return result
  return _wrapper

@time_measure
def linear_search(number: int, array: List[int]) -> bool:
  return number in array

@time_measure
def binary_search(needle: int, haystack: List[int]) -> bool:
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

def print_result(condition: bool) -> None:
  print("found" if condition else "not found")

if __name__ == '__main__':
  print_result(binary_search(NUMBER, ARRAY))
  print_result(linear_search(NUMBER, ARRAY))