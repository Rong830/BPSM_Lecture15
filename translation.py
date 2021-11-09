#!/usr/local/bin/python3

def translate_dna(dna): 
    last_codon_start = len(dna) - 2 
    protein = "" 
    for start in list(range(0,last_codon_start,3)): 
        codon = dna[start:start+3].upper()
        aa = gencode.get(codon,"X") 
        protein = protein + aa 
    return protein 

# top strand frames, all that is changing is the start position, need to just add it to the function arguments
# bottom strand frames, input dna needs to be reverse complemented, then can be processed in exactly the same way as the top strand ones
def translate_dna_2(dna,frame=1): 
    dna=dna.upper()
    if frame not in [-3,-2,-1,1,2,3]:
       print("Not a valid translation frame,\nHas to be one of these: -3, -2, -1, 1, 2, 3.\nExiting....")
       return
    if frame in [-3,-2,-1]:
       print("Need to make the reverse complement to do the reverse strand translations....")
       c_dna = dna.replace("G","c").replace("A","t").replace("T","a").replace("C","g").upper()
# no real builtin reverse method, reversed() produces a different kind of object that we dont really want to deal with!
# the following method is called a slice, and is not only very fast, but also regenerates as a string, which is what we do want
       rc_dna = c_dna[::-1]       
       print("Was\n",dna,"\nnow\n",rc_dna)
       dna = rc_dna
    framestart = abs(frame) - 1
    last_codon_start = len(dna) - ( 2 )   
    protein = "" 
    for start in list(range(framestart,last_codon_start,3)): 
        codon = dna[start:start+3]
        aa = gencode.get(codon,"X") 
        protein = protein + aa 
    return protein


