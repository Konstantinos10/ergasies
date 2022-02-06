file = "two_cities_ascii.txt"
f = list(open(file, "r").read())
l = len(f)
for i in range(l):        
    x = list(bin(ord(f[i])))[2:]
    x = ['0' for i in range(7-l)] + x
    f[i] = ''.join(x[:2] + x[-2:])

b = [''.join(f[i:i+4]) for i in range(0, l, 4)]
l = l//4 + 1

def div(d, x, l):
    s = 0
    for i in x:
        if int(i, 2)%d == 0:
            s += 1
    
    print(100*s/l, '% διαιρείται με το', d)

div(2, b, l)
div(3, b, l)
div(5, b, l)
div(7, b, l)

cmd_wont_close = input()
