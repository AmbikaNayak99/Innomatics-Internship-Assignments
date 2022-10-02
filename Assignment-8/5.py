import math

a = int(input())
b = int(input())
m = int(input())
sig = int(input())

m_sum = b * m 
sig_sum = math.sqrt(b) * sig

def central(a, m, sig):
    from math import erf
maxi = float(input())
n = int(input())
m = float(input())
std = float(input())
mean = n*m
stand = std*(n**0.5)
result = lambda x : 0.5*(1+erf((x-mean)/(stand*(2**0.5))))
p = result(maxi)
p = round(p, 4)
print(p)Z = (a - m)/sig
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(central(a, m_sum, sig_sum), 4))