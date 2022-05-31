''' Creat a function in python which returns the factorial of the input number
'''
def fact(x):
  s=1
  for i in range(1,x+1):
    s*=i
   return s

n=int(input())
out=fact(n)
print(out)
