#Sidhant Puntambekar
#Project-Rosalind Problem 3 Problem Statement:

# Reverse Complement
# ==================
# 
# In a DNA string, the complement of A is T, and the complement of C is G.
# 
# The reverse complement of a DNA string s is the string sc formed by reversing 
# the symbols of s, then taking the complement of each symbol (e.g., the reverse
# complement of GTCA is TGAC).
# 
# Given: A DNA string s of length at most 1000 bp.
# 
# Return: The reverse complement of s.
# 
# Sample Dataset
# --------------
# AAAACCCGGT
# 
# Sample Output
# -------------
# ACCGGGTTTT

def reverse_complement(dataSet):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'} #Dictionary for complementation
    
    sc = reversed(dataSet)
    sc = [complements[i] for i in sc]

    return ''.join(sc)

if __name__ == "__main__":

    example = "AAAACCCGGT"
    rosalind = ""

    print (reverse_complement(example))