from Bio.Seq import Seq


def count_nucleotides(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")

def count_nucleotides_2(s):
    freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in s:
        freq[i] = freq[i] + 1
    return freq['A'], freq['C'], freq['G'], freq['T']


if __name__ == "__main__":
    s = "TCCTCGGGGACTTTCGCGCGACAACTGCGCAGATGTTGCGTGTAGGGCCGAAATATCCCCGCAACTTGAGAGCTCTGGAGACGCATTCACGAAACGCATCTAAGCTCGCGGTACAGAACGGTACGATTGGGCATCCGATATGCTGCATGTGATAGTGCGTTCGAAATCCTGCTGGGCCCGTGGCCATTGCTTCCAATCATCCGACCTAGTTTACCATGTCTGGCTTTGAACGGGAGGAACTCGCACACGAAAAAGCTACAGGCAGCCCCATCCGGATATCATCATGAGGGGGACTCTGGTCCATATTATAGTATTATCAATGTCATCTGTTAGTGCACGAGCTGTTTGTCTGCTGCTACGATCACCGACACGTTCGGTGGGGGGCCTTCGTTGTGGCCGTGAGATCAGCCCTGTGGCGCGTGGTCTAAGCTTTAGGCTAGCTAGGAGTGGCACGCTCGTTGGACCAATCGATTGAATACCTTGCCCATATGTCTGGACAAGGTGTGGGGGACGGTCCGGCGTGCCCTAGATCTGTCATATACGGCTTTGATCTCTTCATCTTCTCAGTCTATTAGTGGTCTATACATTCTAACCCCATTTAGTCCCTTGTGGAACTATACTTGGAATGAAGCACTCATCTGGAGGGGGGTGATGTCTTCCTTCGCCTGCCGAGAAACACTATACGTCGATCGCCCCCGCGTCGCCCCCTCATATTTAACCTGCATTTTTTTCCCCATAGGGAACACCGAAATTACGAGTGGCACACACGTACTATATTCGATGTGTAGTCCGGTTGCATTCGCCCGTGGACCA"
    my_seq = Seq(s)
    print my_seq.count("A"), my_seq.count("C"), my_seq.count("T"), my_seq.count("G")
    print ' '.join(map(lambda x: str(my_seq.count(x)), ['A', 'C', 'T', 'G']))
