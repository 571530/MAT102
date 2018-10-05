# -*- coding: utf-8 -*-
import rsa as rsa
import numpy as np

n=115912873
e=133

alfabet="abcdefghijklmnopqrstuvwxyz"


def fraTallTilTekst(tall, max_antall_tegn):
    if (max_antall_tegn == 0) :
        return ""
    bokstav = tall % 100 
    if (bokstav == 99) :
        return fraTallTilTekst(tall // 100, max_antall_tegn-1) + " "
    return fraTallTilTekst(tall // 100, max_antall_tegn-1) + alfabet[bokstav]

# Oppgave a
dead=[alfabet.find("d"), alfabet.find("e"), alfabet.find("a"), alfabet.find("d")]
dead_encrypted = []
for c in dead: 
    dead_encrypted.append(rsa.powermod(c, e, n))

print(dead)
print(dead_encrypted)

# Oppgave b
primtall = rsa.generate_primes(2, int(np.sqrt(n)))
#print(primtall)

# Oppgave c
p_q = [tall for tall in primtall if n % tall == 0][0]
p = p_q
q = int(n / p_q)

print(p, q)

# Oppgave d
phi = (p-1)*(q-1)
(g, y, x) = gcd(phi, e)
d = x

print((d * e) % ((p - 1) * (q - 1)))

# Oppgave e
print([powermod(c, d, n) for c in dead_encrypted])

secret=[88709091, 115282881, 44754833, 5274204, 37162740, 69569552, 73765472]


print([powermod(c, d, n) for c in secret])
print(''.join([fraTallTilTekst(powermod(c, d, n), 4) for c in secret]))

