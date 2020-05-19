#Sidhant Puntambekar
#Project-Rosalind Problem 2 Problem Statement:

# RNA Transcription
# =================
# 
# An RNA string is formed from the alphabet containing A, C, G, and U.
# 
# Given a DNA string t corresponding to a coding strand, its transcribed RNA 
# string u is formed by replacing all occurrences of T with U.
# 
# Given: A DNA string t of length at most 1000 nucleotides.
# 
# Return: The transcribed RNA string of t.
# 
# Sample Dataset
# --------------
# GATGGAACTTGACTACGTAAATT
# 
# Sample Output
# -------------
# GAUGGAACUUGACUACGUAAAUU

def transcribeRNA(DNA):
    return DNA.replace('T','U')

if __name__ == "__main__":

    sample_dataSet = "GATGGAACTTGACTACGTAAATT"
    rosalind_Dataset = "GTCTGGCGTGGCCCGCGGGCTAGGATAGTAGCCCGACTGCCGCTCCAACGTGGTTCCTTGCGCCATATTAGGGATGAATGGAGAGACGGGTGGCAGATGCACATACAATCGTCTGACTCCCTCCGATAAAGAGCAGCATGATCGAGAAAAACTAGAGAGACCCCCGTAGTATCTGATGAGGTTCTCGACGTTGGGCGTTCCAACCTGCCATTTGTCATGATTCTCGCGCGGGAAACGTAACACGCTACAGACGCCACCCGGTAATTCATTGGGTTTTGCCCAGTCCAGCGATTCATGCCGGTGTTAAGAACGCGAATGCATTACCGATCTCCTCCTAGTCTAGGTCTTTGAGATGAGCGGACTCATTAATCTCAGCGACCAAGTCCCAGCTGATCCTGCCATGATACACTTCTTTCTAGGTAGCACGTAAAAGACGACTTATGACCACCTAACATGCTTTCCGCTGGGGTAACGCTGCCTGATCGTGTAACCGGACCCCGCGAATCTGGGCTATACGCTTGACGTCTGTGGGAACTGGCTAAGCAAGTTGCCATAATTCATATCTCCCAGCTCCCAAGTTGGTTTCGTGTCTACGCCTTTACCGTTCTTGACCTGATACTCTCTGGTCACACACCTATCCCGTGGACTTTCCGTATTCCGCAGATTTGGTTTTACACTTTCGTCGCGCCGCCGCATGCATATACCCCAAACATCCCGCCCCTAGACTAATTATAGGTGTCCTAAGGCGTCAGGTAGATTAAGTTGTTCTAAGTTCGCGGTTAGAAAAAAGATTCGGGAAGTTTCCGTGGCACTATTGGTAAGGCCTCTCCGAACCTTATATCGACCTTTCTTCTAGATTTGGTTATCTACCAAACGCTCCACTAACTTAGGCGGTTAAACCGTAAGTACGT"
    print (transcribeRNA(sample_dataSet))
    print (transcribeRNA(rosalind_Dataset))