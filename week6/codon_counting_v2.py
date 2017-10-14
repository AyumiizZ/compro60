##################################################
## Problem: codon_counting_v2.py
## Std: std61
## Name: 
## StudentId: 
##################################################
RNA = input('Enter RNA: ')
side = input('Left side is (5\' or 3\'): ')
stop = False
count = 0
amino_dict = {'UUU':'Phenylalanine (Phe)','UUC':'Phenylalanine (Phe)','UUA':'Leucine (Leu)','UUG':'Leucine (Leu)','CUU':'Leucine (Leu)','CUC':'Leucine (Leu)','CUA':'Leucine (Leu)','CUG':'Leucine (Leu)','AUU':'Isoleucine (Ile)','AUC':'Isoleucine (Ile)','AUA':'Isoleucine (Ile)','AUG':'Methionine (Met)','GUU':'Valine (Val)','GUC':'Valine (Val)','GUA':'Valine (Val)','GUG':'Valine (Val)','UCU':'Serine (Ser)','UCC':'Serine (Ser)','UCA':'Serine (Ser)','UCG':'Serine (Ser)','CCU':'Proline (Pro)','CCC':'Proline (Pro)','CCA':'Proline (Pro)','CCG':'Proline (Pro)','ACU':'Theronine (Thr)','ACC':'Theronine (Thr)','ACA':'Theronine (Thr)','ACG':'Theronine (Thr)','GCU':'Alanine (Ala)','GCC':'Alanine (Ala)','GCA':'Alanine (Ala)','GCG':'Alanine (Ala)','UAU':'Tyrosine (Tyr)','UAC':'Tyrosine (Try)','CAU':'Histidine (His)','CAC':'Histidine (His)','CAA':'Glutamine (Glu)','CAG':'Glutamine (Glu)','AAU':'Asparagine (Asn)','AAC':'Asparagine (Asn)','AAA':'Lysine (Lys)','AAG':'Lysine (Lys)','GAU':'Aspartic acid (Asp)','GAC':'Aspartic acid (Asp)','GAA':'Glutamic acid (Glu)','GAG':'Glutamic acid (Glu)','UGU':'Cysteine (Cys)','UGC':'Cysteine (Cys)','UGG':'Tryptophan (Trp)','CGU':'Arginine (Arg)','CGC':'Arginine (Arg)','CGA':'Arginine (Arg)','CGG':'Arginine (Arg)','AGU':'Serine (Ser)','AGC':'Serine (Ser)','AGA':'Arginine (Arg)','AGG':'Arginine (Arg)','GGU':'Glycine (Gly)','GGC':'Glycine (Gly)','GGA':'Glycine (Gly)','GGG':'Glycine (Gly)'}
amino_count = {}
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
        if amino_dict[codon] not in amino_count:
            amino_count[amino_dict[codon]] = 1
        else:
            amino_count[amino_dict[codon]] += 1
        i+=3
if count > 0:
    print("***************************")
    for key in sorted(amino_count):
        print("* {:22}{} *".format(key,amino_count[key]))
    print("***************************")
    print("Codon (all): {}\nFound stop codon: {}".format(count,stop))
else:
    print("Cannot find start codon")
