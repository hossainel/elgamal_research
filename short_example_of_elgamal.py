#python utf-8 hossainel
import random
#prime number list
primes = [997,9973,99991] # needs a large amount of prime numbers
#key generation
p = primes[random.randint(0,len(primes)-1)] #gets a random prime number p
#public key g, y and private key x
g, x = random.randint(0,p-1), random.randint(0,p-1)
y = (g**x) % p
def e(g,p,y,m): #encryption
	k = random.randint(2,p-2) #random key k
	r, c = (g**k) % p, (m * y**k) % p
	return (r,c) # returning encrypted msg c1(r,c)
def d(r,c,p,x): return (c * r**(p-x-1)) % p #decryption
result = 0
for m in range(0,128): # test all 128 bit results
	c1 = e(g,p,y,m)
	dk = d(c1[0],c1[1],p,x)
	if (m==dk): result += 1 # check if passes
print(result,g,p,x,y) #print total results
