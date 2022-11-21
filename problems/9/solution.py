"""Problem 9. Palindrome Number
"""

def solution(x):
  # If x is a negative number, it is not a palindrome.
  # If x ends with a zero, it is not a palindrome, unless it is only zero.
  if (x < 0 or (x % 10 == 0 and x != 0)):
    return False

  # Reverse x halfway, store into y.
  y = 0
  while x > y:
    y = (y * 10) + (x % 10)
    x = x // 10

  # If x equals y, or x equals y without the least significant digit (in case of odd, where middle digit is irrelevant) then it is a palindrome.
  return x == y or x == y // 10
