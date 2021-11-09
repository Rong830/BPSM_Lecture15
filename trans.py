#!/usr/local/bin/python3


def translation(dna = "AATGATCGATCGTACGCTGA"):
    if type(dna) != str:
        return print("Your DNA is not a string!")
    a = list(set(list(dna)))
    a.sort()
    if a != ['A', 'C', 'G', 'T']:
        print("Your DNA contains strange base.")
    trans = []
    for i in range(0, len(dna), 3):
        if i + 3 <= len(dna):
            trans.append(gencode[str(dna.upper()[i:i+3])])
    return trans

def reverse_trans(dna):
    dna = dna[::-1]
    translation(dna)
    return translation(dna)

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
   

translation(input("Please enter your DNA string: ")
reverse_trans(input("Please enter your DNA string and I will reverse it then translate it: ")
