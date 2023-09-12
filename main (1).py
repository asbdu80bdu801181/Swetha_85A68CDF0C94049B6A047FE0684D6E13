def factorial(n):
  if not ((n >= 0) and (n % 1 == 0)):
    return ("Number can't be negative or floating point!")
  return 1 if n == 0 else n * factorial(n - 1)


print("\nFactorial of 5: ", factorial(5))
print("\nFactorial of -12: ", factorial(-12))
print("\nFactorial of 1.22: ", factorial(1.22))
print("\nFactorial of 100: ", factorial(100))
