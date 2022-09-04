#python utf-8 hossainel
import random
#prime number list
primes = [997,9973,99991] # needs a large amount of prime numbers
#key generation
p = primes[random.randint(0,len(primes)-1)] #gets a random prime number p
g, x = random.randint(0,p-1), random.randint(0,p-1) #public key g and private key x
def e(g,p,m): #encryption
	k, y = random.randint(2,p-2), (g**x) % p #random key k and generated key y
	r, c = (g**k) % p, (m * y**k) % p
	return (r,c) # returning encrypted msg c1(r,c)
def d(r,c,p,x): return (c * r**(p-x-1)) % p #decryption
result = 0
for m in range(0,128): # test all 128 bit results
	c1 = e(g,p,m)
	dk = d(c1[0],c1[1],p,x)
	if (m==dk): result += 1 # check if passes
print(result,g,p,x,y) #print total results
