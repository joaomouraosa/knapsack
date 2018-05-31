# Merkle–Hellman knapsack 

## keygen(k)
- returns a tuple (p,s,m,n)
- p is the public key
- s is the private key
- m and n are the multiplier and the modulus used to generate the private key from the public key.

## cipher(msg, p)
- returns the cipher

## decipher(msg, s, m, n)
- deciphers msg into the original message.
