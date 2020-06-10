def mutate():
    file1 = open("dna.txt", "r+")
    
#the following funtion "\n" characters messing with the DNA sequence, 
#The following project translate a string containing a nucleotide sequence into 
#a string containing the corresponding sequence of amino acids .
#Nucleotides are translated in triplets using the aminoacids base dictionary;
#each aminoacid 4 is encoded with a string of length 1.

    #Genectic code/mapping of amino acids to single letters which is the key for this translation
AMINOACIDS_BASE = {
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
        
#instead of writting a regualr for loop i am using a rage from 0 - to the length of the SLC/ORF - to step 3
        
def Condons2Protein(SLC, AMINOACIDS_BASE ):
   protein=''
   if len(SLC)%3==0:
    for i in range(0,len(SLC),3):
     codon= SLC[i:i+3]#anytime we take out a triplet nuclotide using the dic we coverst a codon to an aminoacids
    protein += AMINOACIDS_BASE[ codon ]
    return protein
#convert a string on nucletides into a single letter formart
#Test function
Condons2Protein("GAG", AMINOACIDS_BASE)



#so by normalDNA.replace we are cleaning them off the sequence.
    normalDNA = file1.read()
    normalDNA = normalDNA.replace("\n", "") #   Once we read the file we replace all line breaks with "".
    #replacing the small letter a with Capital A
    normalDNA = normalDNA.replace("a", "A")    
    file1.close()

    
    file2 = open("normalDNA.txt", "w")

    file2.write(normalDNA)

    file2.close()

    file1 = open("dna.txt", "r+")

    normalDNA = file1.read()
    normalDNA = normalDNA.replace("\n", "")

    normalDNA = normalDNA.replace("a", "T")

    file1.close()

    file3 = open("mutatedDNA.txt", "w")

    file3.write(normalDNA)

    file3.close()


def txtTranslate():
    file2 = open("normalDNA.txt", "r")
    file3 = open("mutatedDNA.txt", "r")

    return file2.read() + "\n" + file3.read()

mutate()
print(txtTranslate())
