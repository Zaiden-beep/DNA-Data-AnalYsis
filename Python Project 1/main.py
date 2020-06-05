#open the dna .txt file
import importlib
moduleName = input('dna.txt')
importlib.import_module(moduleName)

inputfile="dna.txt" #make sure to put your file in the right directory
f=open(inputfile,"r")
seq=f.read()
# >>>seq   #check the DNA sequence
seq=seq.replace("\n","") #you will see "\n" characters messing with the DNA sequence, so by seq.replace we are cleaning them off the sequence.
seq=seq.replace("\r","")
# >>>seq   #check the DNA sequence
def translate(seq):
    """
    Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids .
    Nucleotides are translated in triplets using the aminoacids base dictionary; each amino acid 4 is encoded with a string of length 1.
    """
    AMINOACIDS_BASE = {'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'TTA': 'L', 'TTG': 'L',
'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
'TTT': 'F', 'TTC': 'F',
'ATG': 'M'}
        
    protein=""
    if len(seq)%3==0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protein+=AMINOACIDS_BASE[codon]
    return protein
def mutate(inputfile):
    with open(inputfile,"r") as f:
        seq=f.read()
    seq=seq.replace("\n","")
    seq=seq.replace("\r","")
    return seq

prt = mutate("normalDNA.txt")
dna = mutate("mutatedDNA.txt")
# >>>translate(dna)
# >>>translate(dna[20:938])  translating the DNA sequence
p = translate(dna[20:935]) #character = tri base pair
p == prt 

