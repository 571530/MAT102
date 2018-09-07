def caesar(txt, rotate) :
	crypt = ""
	for char in txt:
		if ord(char) >= ord('a') and ord(char) <= ord('z'):
			crypt = crypt + chr((ord(char) - ord('a') + rotate) % 26 + ord('a'))
	return crypt

def frequencyOfString(file):
	frekvenser = [0]*26

	antall = 0
	with open(file) as f:
		for line in f:
			for ch in line:
				c = ch.lower()
				if ord(c) >= ord('a') and ord(c) <= ord('z'):
					frekvenser[ord(c)-ord('a')] += 1
					antall += 1

	return [x / antall for x in frekvenser]

def compareFrequency(comp, ref):
	sum = 0;
	for i in range(0, 26):
		sum += ((comp[i] - ref[i])**2) / ref[i]
	return sum

def oppgave1():
	for i in range(0, 26):
		print(caesar("xcy", i))
			

def oppgave2():
	for i in range(0, 26):
		txt = caesar("xcy", i)
		if txt.count('e') > 0:
			print(txt)	

def oppgave4():
	comp = frequencyOfString("romeoogjuliet.txt")
	ref = frequencyOfString("macbeth.txt")
	print(compareFrequency(comp, ref))

def oppgave5():
	for i in range(0, 26):
		txt = caesar("uibpmuibqkaqauwzmncvbpivxzwoziuuqvo", i)
		if txt.count('e') > 1:
			print(txt)	


oppgave4()
