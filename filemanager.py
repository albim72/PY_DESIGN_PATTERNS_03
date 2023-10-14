class FileManager:
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __repr__(self):
        return "tworzymy dostęp do operacji na pliku..."

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# fm = FileManager("takie.txt","r","utf-8")
# print(fm)

with FileManager('test.txt','w','utf-8') as f:
    f.write('to jest ważna treść > abcd456')
    print(type(f))

print(f.closed)

with open('abc.txt','w',encoding='utf-8') as d:
    d.write("fhsdkllfdkfjd 4008989")

print(d.closed)

with FileManager('test.txt','r','utf-8') as f:
    print(f.read())
