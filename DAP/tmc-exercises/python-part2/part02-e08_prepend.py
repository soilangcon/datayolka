class Prepend(object):
    def __init__(self, start):
        self.start = start 
    def write(self, prepend):
        print(f"{self.start}{prepend}")

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
