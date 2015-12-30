def slicing_practice(s, a, b, c, d):
    return s[a:b+1] + " " + s[c:d+1]

def conditions_and_loops(a, b):
    return sum(i for i in range(a, b + 1) if i % 2 == 1)

def conditions_and_loops_2(a, b):
    return sum(range(a | 1, b + 1, 2))

def even_lines(filename):
    f = open(filename, 'r')
    newFile = open('output.txt', 'w')
    i = 0
    for line in f:
        if i % 2 == 1:
            newFile.write(line)
        i += 1

def even_lines_2(filename):
    with open(filename, 'r') as f:
        print ''.join(f.readlines()[1::2])

def frequencies(filename):
    f = open(filename, 'r')
    newFile = open('frequencies.txt', 'w')
    frequencyDict = {}
    for line in f:
        for word in line.split():
            if word in frequencyDict:
                frequencyDict[word] += 1
            else:
                frequencyDict[word] = 1

    for key in frequencyDict:
        newFile.write(str(key + ' ' + str(frequencyDict[key]) + '\n'))

def frequencies_2(filename):
    with open(filename, 'r') as f:
        from collections import Counter
        for k, v in Counter(str(f.readlines()).split()).items():
            print(k, v)
