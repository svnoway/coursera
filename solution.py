class FileReader:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        try:
            file = open(self.filename)
            return file.read()
        except IOError:
            return ""
def main():
    x = FileReader('example.txt')
    print(x.read())
if __name__ == "__main__":
    main()