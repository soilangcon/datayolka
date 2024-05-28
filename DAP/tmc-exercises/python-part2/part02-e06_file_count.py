import sys

def file_count(filename='test.txt):
    linecount, wordcount, lettercount = 0, 0, 0
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1
            words = line.split()
            wordcount += len(words)
            lettercount += len(line)
    return (linecount, wordcount, lettercount)

def main():
    for filename in sys.argv[1:]:
        lines, words, chars = file_count(filename)
        print(f"{lines}\t{words}\t{chars}\t{filename}")

if __name__ == "__main__":
    main()
