#Sidhant Puntambekar
#Project-Rosalind Problem 4 Problem Statement:

# Given: Positive integers
# n < 40 and k < 5 
# .

# Return: The total number of rabbit pairs that will be present after n
# n
#  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
# k
#  rabbit pairs (instead of only 1 pair).

def fibonacci(n, k):
  if (n == 1):
      return 1
  elif (n == 2):
      return 1
  else:
      return fibonacci(n-1, k) + fibonacci(n-2, k)*k

if __name__ == '__main__':
    print(fibonacci(28,3))