__author__ = 'rainierababao'

seq1 = str(raw_input("Genome sequence: "))
seq2 = str(raw_input("Read sequence: "))
seq1 = seq1.upper()
seq2 = seq2.upper()
print "Your genome ref input : " +seq1
print "Your read ref input   : " +seq2

matrix = []
path = []
row = len(seq2)
col = len(seq1)
seq2 = "^"+seq2
seq1 = "^"+seq1
for i in range(row+1):
    matrix.append([0]*(col+1))
    path.append(["N"]*(col+1))

def print_matrix(matrix):
    print '\t'+('\t'.join(map(str,list(seq1))))
    i = 0
    for line in matrix:
        print seq2[i]+"\t"+('\t'.join(map(str,line)))
        i +=1

indelValue = -1
matchValue = 2
for i in range(1,row+1):
    for j in range(1,col+1):
        # penalty map
        from_left = matrix[i][j-1] + indelValue
        from_top = matrix[i-1][j] + indelValue
        if seq2[i]==seq1[j]:
            from_diag = matrix[i-1][j-1] + matchValue
        else:
            from_diag = matrix[i-1][j-1] + indelValue

        matrix[i][j]= max(from_left,from_top,from_diag)
        # path map
        if matrix[i][j]==from_left:
            path[i][j]="-"
        elif matrix[i][j]==from_top:
            path[i][j] = "|"
        elif matrix[i][j] == from_diag:
            path[i][j] = "M"
        else:
            pass

        if matrix[i][j]<0:
            matrix[i][j]=0
pass
print_matrix(matrix)
print
print_matrix(path)

rowWB = len(matrix)-1
colWB = len(matrix[0])-1

while rowWB>=0:
    maxPnltyVaue = max(matrix[rowWB])
    while colWB>=0:
        if matrix[rowWB][colWB]==maxPnltyVaue:
            rowPair = rowWB
            colPair = colWB
            reportSeq2=[]
            reportSeq1=[]
            while (1):
                if rowPair ==0 and colPair==0:
                    break
                if path[rowPair][colPair]=="M":
                    reportSeq2.append(seq2[rowPair])
                    reportSeq1.append(seq1[colPair])
                    rowPair -= 1
                    colPair -= 1
                elif path[rowPair][colPair]=="-":
                    reportSeq2.append("-")
                    reportSeq1.append(seq1[colPair])
                    colPair -= 1
                elif path[rowPair][colPair]=="|":
                    reportSeq2.append(seq2[rowPair])
                    reportSeq1.append("-")
                    rowPair -= 1
                elif path[rowPair][colPair]=="N":
                    if rowPair > 0:
                        reportSeq2.append(seq2[rowPair])
                        rowPair -=1

                    if colPair > 0:
                        reportSeq1.append(seq1[colPair])
                        colPair -= 1

            print "Your alignment would be followed: "
            print "R:"+ "".join(reversed(reportSeq2))
            print "G:"+ "".join(reversed(reportSeq1))
            print
        colWB -=1
    rowWB -=1