import re
from string import maketrans
from Bio.Seq import translate

orig_sequence = """""".replace('\n', '')
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')

def get_reverse_complement(dna_seq):
    return dna_seq[::-1].translate(maketrans("ATGC","TACG"))

def get_open_reading_frames(dna):
    return set(pattern.findall(dna) + pattern.findall(get_reverse_complement(dna)))

print '\n'.join(map(lambda seq: translate(seq), get_open_reading_frames(orig_sequence)))
