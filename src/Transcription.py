def transcribe():
    print raw_input().replace('T', 'U')

if __name__ == '__main__':
    t = raw_input()
    result = ""
    for letter in transcribe(t):
        result = result + letter
    print result
    transcribe()
