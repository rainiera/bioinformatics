from string import maketrans


def reverse_complement(s):
    sc = s.replace("A", "X").replace("C", "Y").replace("T", "A").replace("G", "C").replace("X", "T").replace("Y", "G")
    sc = sc[::-1]
    return sc

def reverse_complement_2(s):
    sc = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return sc

def reverse_complement_3(s):
    return s[::-1].translate(maketrans('ACGT', 'TGCA'))


if __name__ == "__main__":
    # print reverse_complement(raw_input())
    # print reverse_complement_2(raw_input())
    print reverse_complement_3(raw_input())
