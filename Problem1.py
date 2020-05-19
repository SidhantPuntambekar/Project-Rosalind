#Sidhant Puntambekar
#Project-Rosalind Problem 1 Problem Statement:

# A string is simply an ordered collection of symbols selected from some
# alphabet and formed into a word; the length of a string is the number of
# symbols that it contains.
# 
# An example of a DNA string (whose alphabet contains the symbols A, C, G, 
# and T) is "ATGCTTCAGAAAGGTCTTACG".
# 
# Given: A DNA string s of length at most 1000 nt.
# 
# Return: Four integers separated by space corresponding to the number of 
# times that the symbols A, C, G, and T occur in s.
#
# Sample Dataset
# --------------
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
#
# Sample Output
# -------------
# 20 12 17 21

def DNA(dataSet):
  a = 0
  c = 0
  g = 0
  t = 0
  for i in dataSet:
    if (i == 'A'):
      a += 1
    if (i == 'C'):
      c += 1
    if (i == 'G'):
      g += 1
    if (i == 'T'):
      t += 1
  print (str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))

DNA("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")