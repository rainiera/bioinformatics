__author__ = 'rainierababao'

"""
Local sequence alignment using the Smith-Waterman algorithm.

Takes a sequence from a genome and a sequence to be aligned.

Returns the alignment between the two parameters.

Typically the sequences are from nucleotides or proteins,
but the concept can be extended to strings or lists in general.

For more information, check out the Wikipedia article:
http://en.wikipedia.org/wiki/Smith-Waterman_algorithm
"""

# TODO fix an index out of range error that kept occurring during tests

def prompt():
    seq1 = str(raw_input("Enter genome sequence: "))
    seq2 = str(raw_input("Enter sequence to align: "))
    askCase = str(raw_input("Case sensitive alignment - y/n?: ")).upper()
    caseSensitive = askCase == "Y"

# makes the sequences the same case if chosen by the user
def normalize():
    seq1.upper()
    seq2.upper()

# void, generates a matrix
def generateMatrix(seq1, seq2):
    for i in range(1, numRows):
        matrix.append([0] * numCols)
        path.append(["N"] * numCols)

# void, prints the matrix
def printMatrix(matrix):
    print "\t" + ("\t".join(map(str, list(seq1))))
    i = 0
    for line in matrix:
        print seq2[i] + "\t" + ("\t".join(map(str, line)))
        i += 1

# s, short for similarity function
# returns the result of the similarity function
def s(a, b):
    if a == b:
        return 2
    if a != b:
        return -1

# void, generates the penalty map
def penaltyMap(m, p):
    for i in range(1, numRows):
        for j in range(1, numRows):
            left = m[i][j-1] - 1
            top = m[i-1][j] - 1
            diag = m[i-1][j-1] + s(seq2[i], seq1[j])

            m[i][j] = max(left, top, diag)

            if m[i][j] == left:
                p[i][j] = "-"
            elif m[i][j] == top:
                p[i][j] = "|"
            elif m[i][j] == diag:
                p[i][j] = "M"
            else:
                pass

            if m[i][j] < 0:
                m[i][j] = 0
    pass

# void, traverses the penalty map in order to construct the alignment
def walkback():
    rowWB = len(matrix) - 1
    colWB = len(matrix[0]) - 1

    while rowWB >= 0:
        maxPenalty = max(matrix[rowWB])
        while colWB >= 0:
            if matrix[rowWB][colWB] == maxPenalty:
                rowPair = rowWB
                colPair = colWB
                while (1):
                    if rowPair == 0 and colPair == 0:
                        break
                    if path[rowPair][colPair] == "M":
                        resultSeq2.append(seq2[rowPair])
                        resultSeq1.append(seq1[colPair])
                        rowPair -= 1
                        colPair -= 1
                    elif path[rowPair][colPair] == "-":
                        resultSeq2.append("-")
                        resultSeq1.append(seq1[colPair])
                        colPair -= 1
                    elif path[rowPair][colPair] == "|":
                        resultSeq2.append(seq2[rowPair])
                        resultSeq1.append("-")
                        rowPair -= 1
                    elif path[rowPair][colPair] == "N":
                        if rowPair > 0:
                            resultSeq2.append(seq2[rowPair])
                            rowPair -= 1

                        if colPair > 0:
                            resultSeq1.append(seq1[colPair])
                            colPair -= 1

            colWB -= 1
        rowWB -= 1

def results():
    print "The alignment: "
    print "Analyze sequence: " + "".join(reversed(resultSeq2))
    print "Genomic sequence: " + "".join(reversed(resultSeq1))
    print ""

if __name__ == '__main__':
    # declare vars for main operation
    seq1 = ""
    seq2 = ""
    caseSensitive = True

    prompt()
    if not caseSensitive:
        normalize()

    # declare matrix vars and generate the matrix
    numRows = len(seq1) + 1
    numCols = len(seq2) + 1
    matrix = []
    path = []
    generateMatrix(seq1, seq2)

    # generate the penalty map and print the matrices
    penaltyMap(matrix, path)

    printMatrix(matrix)
    printMatrix(path)

    # generates the reporting matrices and performs the walk back
    resultSeq1 = []
    resultSeq2 = []
    walkback()

    results()
