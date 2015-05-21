__author__ = 'rainierababao'

"""
Interestingly enough, this happens to be 10x faster than tracking the counts
manually with a dictionary, even though the dictionary solution only iterates
through the string once, rather than four times.

Apparently "count" is a low-level C method in Python so it's much faster.
Map generates an iterator,
"""

def count_nucleotides(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")

"""
The iterating through a dictionary solution. Theoretically smaller time complexity
since it only iterates the nucleotide sequence once instead of four times.
"""

def count_nucleotides_2(s):
    freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in s:
        freq[i] = freq[i] + 1
    return freq['A'], freq['C'], freq['G'], freq['T']


if __name__== "__main__":
    s = "TCCTCGGGGACTTTCGCGCGACAACTGCGCAGATGTTGCGTGTAGGGCCGAAATATCCCCGCAACTTGAGAGCTCTGGAGACGCATTCACGAAACGCATCTAAGCTCGCGGTACAGAACGGTACGATTGGGCATCCGATATGCTGCATGTGATAGTGCGTTCGAAATCCTGCTGGGCCCGTGGCCATTGCTTCCAATCATCCGACCTAGTTTACCATGTCTGGCTTTGAACGGGAGGAACTCGCACACGAAAAAGCTACAGGCAGCCCCATCCGGATATCATCATGAGGGGGACTCTGGTCCATATTATAGTATTATCAATGTCATCTGTTAGTGCACGAGCTGTTTGTCTGCTGCTACGATCACCGACACGTTCGGTGGGGGGCCTTCGTTGTGGCCGTGAGATCAGCCCTGTGGCGCGTGGTCTAAGCTTTAGGCTAGCTAGGAGTGGCACGCTCGTTGGACCAATCGATTGAATACCTTGCCCATATGTCTGGACAAGGTGTGGGGGACGGTCCGGCGTGCCCTAGATCTGTCATATACGGCTTTGATCTCTTCATCTTCTCAGTCTATTAGTGGTCTATACATTCTAACCCCATTTAGTCCCTTGTGGAACTATACTTGGAATGAAGCACTCATCTGGAGGGGGGTGATGTCTTCCTTCGCCTGCCGAGAAACACTATACGTCGATCGCCCCCGCGTCGCCCCCTCATATTTAACCTGCATTTTTTTCCCCATAGGGAACACCGAAATTACGAGTGGCACACACGTACTATATTCGATGTGTAGTCCGGTTGCATTCGCCCGTGGACCA"
    print count_nucleotides(s)
    print count_nucleotides_2(s)