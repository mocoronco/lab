import math

y = 3
u = 4

n = 4
a = y / u
sum = 0

for i in range(n + 1):
  value = a ** i / math.factorial(i)
  sum += value
  print('k='+str(i)+')', value)

p0 = 1 / sum
print('\np0:', p0, '\n')

for i in range(n):
  i = i + 1
  p = ((a ** i) / math.factorial(i)) * p0
  print('p' + str(i) + ':', p)
  
print('\nn =', n)
  
p_error = p
print('p-отк:', p_error)
p_good = 1 - p_error
print('p-обс:', p_good)
Q = 1 - p_error
print('Q:', Q)
A = p_good * y
print('A:', A)
