file = "two_cities_ascii.txt"
f = list(open(file, "r").read())

for i in range(len(f)): #turning all non letter characters to spaces to be removed later
    if not f[i].isalpha():
        f[i] = " "

f = "".join(f).split() #f contains now only words



w = [] #contains one of every word
wc = [] #the amount of times a word is found

for i in f:
    if not i in w:
        w.append(i)
        wc.append(1)
    else:
        x = w.index(i)
        wc[x] += 1

        if x != 0: #extra optimization(puts the most common words earlier in the list so the index function can find them quicker)
            if wc[x] > wc[x-1]:
                wc[x], wc[x-1] = wc[x-1], wc[x]
                w[x], w[x-1] = w[x-1], w[x]

def f(i):
    return wc[w_copy.index(i)]
w_copy = w[:]
w.sort(reverse=True, key=f)
wc.sort(reverse=True)

for i in range(10):
    print(i+1, w[i], '  ', wc[i], 'εμφανίσεις')
print('')



w2 = [] #contains every x letter combination found
w2c = []

for i in w:
    x = i.lower()
    if len(x) > 1:
        x = x[:2]
        if not x in w2:
            w2.append(x)
            w2c.append(1)
        else:
            w2c[w2.index(x)] += 1

def g(i):
    return w2c[w2_copy.index(i)]
w2_copy = w2[:]
w2.sort(reverse=True, key=g)
w2c.sort(reverse=True)

for i in range(3):
    print(i+1, w2[i], '  ', w2c[i], 'εμφανίσεις')
print('')



w3, w3c = [], []

for i in w:
    x = i.lower()
    if len(x) > 2:
        x = x[:3]
        if not x in w3:
            w3.append(x)
            w3c.append(1)
        else:
            w3c[w3.index(x)] += 1

def h(i):
    return w3c[w3_copy.index(i)]
w3_copy = w3[:]
w3.sort(reverse=True, key=h)
w3c.sort(reverse=True)

for i in range(3):
    print(i+1, w3[i], '  ', w3c[i], 'εμφανίσεις')

cmd_wont_close = input()
