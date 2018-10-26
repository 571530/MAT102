import rsa
import numpy as np
import regression
import matplotlib.pyplot as plt
import pca


# Oppgave 1

# Hjelpe funksjoner for å kode og dekode meldinger

alfabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def fraTekstTilTall(tekst):
    # Del opp strengen i strenger med lengde 4
    delt_tekst = [tekst[start:start+4] for start in range(0, len(tekst), 4)]
    
    res = []
    for mld in delt_tekst:
        tall = 0
        i = 0
        for ch in mld[::-1]: # gå gjennom baklengs
            if ch == ' ':
                tall += 99 * 10**i
            else:
                tall += (ord(ch) - ord('A')) * 10**i
            i+=2
        res.append(tall)
    return res
        

def fraTallTilTekst(tall, max_antall_tegn):
    if (max_antall_tegn == 0) :
        return ""
    bokstav = tall % 100 
    if (bokstav == 99) :
        return fraTallTilTekst(tall // 100, max_antall_tegn-1) + " "
    return fraTallTilTekst(tall // 100, max_antall_tegn-1) + alfabet[bokstav]

# Variabler brukt i oppgaver videre
n = 160169311
e = 1737

# a)
melding = [1041706, 4139999]
for x in melding:
    print(fraTallTilTekst(x, 4), end="") # -> "BERGEN"
print()


# b)
melding = "HEI SJEF"
kodet_melding = fraTekstTilTall(melding)
print(kodet_melding)  # -> [7040899, 18090405]

# c)
kryptert_melding = [rsa.powermod(c, e, n) for c in kodet_melding]
print(kryptert_melding) # -> [58822763, 79142533]

# d)
primtall = rsa.generate_primes(2, int(np.sqrt(n)))

p_q = [tall for tall in primtall if n % tall == 0][0]
p = p_q
q = int(n / p_q)

print(p, q) # -> 11897 13463

# e)
# for at e er gyldig må gcd((p-1)*(q-1), e) == 1

phi = (p-1)*(q-1)
(g, y, x) = rsa.gcd(phi, e)

print(g == 1) # -> True

# f)
d = x % phi
print("".join([fraTallTilTekst(rsa.powermod(c, d, n), 4) for c in kryptert_melding]))
# -> HEI SJEF

# g)
U = [112718817, 85128008, 148479246, 91503316, 26066602, 95584344, 142943071]
print("".join([fraTallTilTekst(rsa.powermod(c, d, n), 4) for c in U]))
# -> "  JEG GLEDER MEG TIL EKSAMEN"

# Oppgave 2

T = [13.14, 12.89, 12.26, 12.64, 12.22, 12.47, 12.51, 12.80, 12.24, 12.77, 13.35, 12.82, 13.57, 13.38, 14.41, 14.00, 15.68, 15.41, 15.51, 15.86, 15.72]
X = [x*3 for x in range(0, len(T))]

plt.figure(1)

# a)
plt.scatter(X, T)

# b)
[a_lin, b_lin] = regression.linearRegression(X, T)

Sy2_lin = sum((T - np.mean(T))**2)
SSE_lin = sum((T - (np.dot(a_lin, X) + b_lin))**2)
R2_lin = (Sy2_lin - SSE_lin) / Sy2_lin

print("Determinantkoeffisient for lineære", R2_lin) # -> 0.7452554736192584

xplot = np.array(list(range(min(X), max(X))))
yplot = np.dot(xplot, a_lin) + b_lin

plt.plot(xplot, yplot)  

# c)
[a_kva, b_kva, c_kva] = regression.quadraticRegression(X, T)

Sy2_kva = sum((T - np.mean(T))**2)
SSE_kva = sum((T - (np.dot(a_kva, np.power(X, 2)) 
                    + np.dot(b_kva, X) + c_kva))**2)
R2_kva = (Sy2_kva - SSE_kva) / Sy2_kva

print("Determinantkoeffisient for kvadratisk", R2_kva) # -> 0.9126314317675248

yplot = np.dot(a_kva, np.power(xplot,2)) + np.dot(b_kva, xplot) + c_kva

plt.plot(xplot, yplot)  


[a_kub, b_kub, c_kub, d_kub] = regression.cubicRegression(X, T)

Sy2_kub = sum((T - np.mean(T))**2)
SSE_kub = sum((T - (np.dot(a_kub, np.power(X, 3)) 
                    + np.dot(b_kub, np.power(X, 2))
                    + np.dot(c_kub, X) + d_kub))**2)
    
R2_kub = (Sy2_kub - SSE_kub) / Sy2_kub

print("Determinantkoeffisient for kubisk", R2_kub) # -> 0.9335598634480327

yplot = np.dot(a_kub, np.power(xplot,3)) + np.dot(b_kub, np.power(xplot,2)) + np.dot(c_kub, xplot) + d_kub

plt.plot(xplot, yplot)  

# d)


# Oppgave 3

# Fylker (alfabetisk, tallene under står i den samme rekkefølgen):
Fylker = ['Akershus','Aust-Agder','Buskerud','Finnmark','Hedmark','Hordaland','Møre og Romsdal','Nordland','Nord-Trøndelag','Oppland','Oslo','Rogaland','Sogn og Fjordane','Sør-Trøndelag','Telemark','Troms','Vest-Agder','Vestfold','Østfold']
Indikatorer = ['Areal','Folketall', 'BNP/kapita','BNP/sysselsatt', 'Sysselsatte']
#Areal målt i kvadratkilometer
Areal = [4917.95,9155.36,14912.19,48631.38,27397.85,15436.98,15101.07,38478.13,22414,25192.09,454.10,9376.77,18622.44,18848,15298.23,25876.85,7278.71,2225.38,4187.22]
# Folketall 1/1 2017
Folketall =[604368,116673,279714,76149,196190,519963,266274,242866,137233,189479,666759,472024,110266,317363,173307,165632,184116,247048,292893]
# BNP og sysselsatte: Tall fra 2017
BNPKap=[435982,337974,397080,438594,364944,488515,433030,428402,367157,363111,820117,488463,455872,473954,371886,451887,403893,364007,331575]
BNPSyss =[918710,771973,831298,808765,777248,922939,834642,850163,759414,731136,1125019,899272,846111,886057,817060,824648,811833,792748,778412]
Sysselsatte=[270338,47868,125938,37143,86627,254290,127060,116020,62621,86968,468375,233986,54490,166479,74749,84537,86997,106931,118320]

X = np.transpose(np.array([Areal,Folketall,BNPKap,BNPSyss,Sysselsatte]))

X = pca.standardize(pca.meanCenter(X))

T, P, E = pca.pca(X, 2)

plt.figure(2)

plt.scatter(T[:,0], T[:,1])
for txt, x, y in zip(Fylker, T[:,0], T[:,1]):
    plt.annotate(txt, xy = (x, y))

plt.scatter(P[:,0], P[:,1])
for txt, x, y in zip(Indikatorer, P[:,0], P[:,1]):
    plt.annotate(txt, xy = (x, y))
    
        
    
# c)
# T plottet gir oss gruperinger av fylkene og P gir oss grupperinger av indikatorene.
# Plotting av begge to heter biplot

# d)
    
    
# e) Oslo

