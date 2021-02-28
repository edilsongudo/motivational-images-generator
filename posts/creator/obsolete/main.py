with open('man.txt', 'r') as f:
    man = []
    mans = f.readlines()
    for frase in mans:
        frase = frase.rstrip()
        man.append(frase)

with open('HomensAlfa.txt', 'r') as f:
    HomensAlfa = []
    mans = f.readlines()
    for frase in mans:
        frase = frase.rstrip()
        HomensAlfa.append(frase)
n = 1
for frase in man:
    if frase in HomensAlfa:
        print(n, frase)
        n += 1
