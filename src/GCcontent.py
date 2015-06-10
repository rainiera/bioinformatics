__author__ = 'rainierababao'

def get_highest_GC(filename):
    f = open(filename, 'r')
    strands = {}

    for line in f.readlines():
        if line[0] == '>':
            id = line.strip('>\n')
        else:
            if id not in strands:
                strands[id] = line.strip('\n')
            else:
                strands[id] += line.strip('\n')

    max, maxId = 0, ''

    for id in strands:
        if get_GC_percentage(strands[id]) > max:
            maxId = id
            max = get_GC_percentage(strands[id])

    return maxId, str(max)


def get_GC_percentage(str):
    return (float((str.count('G') + str.count('C'))) / len(str)) * 100.0

if __name__ == "__main__":
    print get_highest_GC("test.txt")[0] + '\n' + get_highest_GC("test.txt")[1]