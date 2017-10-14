##################################################
## Problem: codon_counting.py
## Std: std61
## Name: 
## StudentId: 
##################################################
RNA = input('Enter RNA: ')
side = input('Left side is (5\' or 3\'): ')
stop = False
count = 0
if side == '3':
    RNA = RNA[::-1]
if 'AUG' in RNA:
	i = RNA.index('AUG')
	while i<len(RNA)-2:
		codon = RNA[i:i+3]
		if codon in ['UAA','UGA','UAG']:
			stop = True
			break
		count+=1
		i+=3
print("Codon: {}\nFound stop codon: {}".format(count,stop))
