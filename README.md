## DNA-Data-AnalYsis

*Lauguage: Python
Create a programme that simulates the effects of a single nucleotide polymorphism that leads to sickle Cell Disease.

• Use the PDF below this message to find a table of all codons and their corresponding amino acids. Note the 'SLC' code for each Amino Acid. 

• Now: Write a function called translate that, when given a DNA sequence of arbitrary length, identifies and returns the amino acid sequence of the DNA using the amino acid SLC code. For example: DNA Input: ATTCTCATA  Output: ILI *

• There are many different amino acids so this may get a bit repetitive. Just do the first five Amino Acids (i.e I L V F M) and print an 'X' for any other codon. Note that the program must be able to handle DNA sequences that are not of a length divisible by 3. 

• Create another function called mutate. This function should read in the contents of the text file named DNA.txt and identify the first occurrence of the lowercase letter 'a' in DNA.txt. You can find the DNAText file in the files section. Two empty text files normalDNA.txt and mutatedDNA.txt can also be found by clicking on the 'Files' button. Write to both of these files. The normalDNA.txt file must contain the same DNA sequence as DNA.txt with the 'a' changed to an 'A'. The mutatedDNA.txt file must contain the same DNA sequence as DNA.txt with the 'a' changed to a 'T'.


• Finally create a new function called txtTranslate, that calls the translate function. Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid sequences to the user.
