import unicodedata

def getpunctuation(filename:str):
    punc = {}
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp:
            for c in line:
                category = unicodedata.category(c)
                if category[0] == "P":
                    punc[c] = True
    return "".join(list(punc))

##print(getpunctuation("hyde.txt"))
##sys.exit(0)



def splitline(line:str) -> list:
    return line.replace("-", " ").split()

def cleanword(word:str, punctuation:str):
    for p in punctuation:
        word = word.replace(p, " ")
    return word.strip().lower()

def readtext(filename:str):
    lines = []
    with open(filename, "r", encoding = "utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line != "":
                 print(line)
                 lines.append(line)
    return lines

punc = getpunctuation("hyde.txt")
lines = readtext("hyde.txt")
uq = {}

for line in lines:
    for word in splitline(line, punc):
        word = cleanword(word, punc)
        ##uq[word] = 1;
        uq[word] = uq.get(word, 0) + 1

def second(item):
    return item[1]

print(sorted(uq.items(), key=lambda item: item[1], reverse=True))


