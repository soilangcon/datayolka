import re

def file_extensions(filename):
    pattern = r'(\w+)[.(\w+)]?\s*'
    filenames, extensions = [], {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            matched = re.findall(pattern, line)
            if len(matched) == 1:
                filenames.append(line)
            else:
                _ , fext = matched[0], matched[-1]
                if fext not in extensions:
                    extensions[fext] = [line]
                else:
                    extensions[fext].append(line)
    return (filenames, extensions)

def main():
    filenames, extensions = file_extensions("filenames.txt")
    print(f"{len(filenames)} files with no extension")
    for fext in extensions:
        print(f"{fext} {len(extensions[fext])}")

if __name__ == "__main__":
    main()
