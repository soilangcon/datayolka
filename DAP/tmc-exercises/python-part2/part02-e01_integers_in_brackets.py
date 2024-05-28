import re

def integers_in_brackets(s):
    # pattern = r'\s*[0-9]+\s*'
    # pattern = r'\s*[+-]?\d+\s*'
    pattern = r'\[\s*([+-]?\d+)\s*\]'
    matches = re.findall(pattern, s)
    # matches = re.finditer(pattern, s)
    # return matches, [match.group() for match in matches] 
    return matches, list(map(int, matches)) 

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
