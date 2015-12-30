"""
Pre: A list of three positive integers k, m, and n, representing a population containing
k + m + n organisms (k = homozygous dominant, m = heterozygous, n = homozygous recessive)
Any two organisms can mate; (k * m * n) > 0

Post: Return the probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant phenotype)
"""

def p_of_dominant_phenotype(kmnList):
    k = kmnList[0]
    m = kmnList[1]
    n = kmnList[2]

    # the denominator for the sum of all the probabilities of picking each two
    denom = (k + m + n) * (k + m + n - 1)

    # each case... could do better
    a = k * (k - 1)     # AAAA
    b = k * m           # AAAa
    c = k * n           # AAaa
    d = m * k           # AaAA
    e = m * (m - 1)     # AaAa
    f = m * n           # AaAa
    g = n * k           # aaAA
    h = n * m           # aaAa
    # no bother including the aaaa case since the probability of having a dom allele is 0

    # the AaAa, Aaaa, and aaAa cases have to be multiplied by the probability of them
    # resulting in at least one dominant allele (easy to check with Punnett square)
    # (every other case is assumed to have probability 1 of having at least one dom allele)
    e = float(e * 0.75)
    f = float(f * 0.5)
    h = float(h * 0.5)

    # add all of them... lol
    x = float(a + b + c + d + e + f + g + h)

    # divide the sum of the numerators of the probabilities
    y = x / (float(denom))
    return y

"""
Same thing but using a probability matrix. Beautiful!!
"""

def p_of_dominant_phenotype_2(homoDom, hetero, homoRec):
    counts = (homoDom, hetero, homoRec)
    denom = sum(counts) * (sum(counts) -1)
    probabilities = ((1.0, 1.0, 1.0), (1.0, 0.75, 0.5), (1.0, 0.5, 0.0))
    dominantProbability = 0
    for i in range(len(counts)):
        for j in range(len(counts)):
            second = counts[j] - 1 if i == j else counts[j]
            dominantProbability += probabilities[i][j] * counts[i] * second / denom
    return dominantProbability

"""
Pre: A list of 6 positive integers, all less than or equal to 20000.
Correspond to the number of couples in a population possessing each genotype pairing
In order, the six integers represent the number of couples having the following genotypes:
1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

Post: Expected number of offspring displaying the dominant phenotype in the next generation,
under the assumption that every couple has exactly two offspring
"""

def expected_value(kmnpqrStr, probabilities):
    kmnpqrList = kmnpqrStr.split(" ")
    sum = 0
    for i in range(0, len(kmnpqrList) - 1):
        sum += float(kmnpqrList[i]) * probabilities[i]
    return sum * 2

"""
Same thing but with a list comprehension
"""

def expected_value_2():
    return sum([a * int(b) for a,b in zip([2, 2, 2, 1.5, 1, 0], '1 0 0 1 0 1'.split())])

if __name__ == "__main__":
    # kmnList = [15, 24, 30]
    # print p_of_dominant_phenotype(kmnList)
    # print p_of_dominant_phenotype_2(15, 24, 30)
    pr = [1.0, 1.0, 1.0, 0.75, 0.5, 0]
    print expected_value("18285 18725 16233 17979 17217 18429", pr)
