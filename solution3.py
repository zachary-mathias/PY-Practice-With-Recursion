# Write code for algorithm 3 below

def fibbonacci(n):
    if n <= 0:
      print("incorrect input")
    elif n == 1:
      return 0
    elif n == 2:
       return 1
    else:
       return fibbonacci(n-1)+fibbonacci(n-2)
    print("2nd fib number:")
print(fibbonacci(2))
print("4th fib number:")
print(fibbonacci(4))
print("8th fib number:")
print(fibbonacci(8))