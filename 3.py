file = "two_cities_ascii.txt"
f = list(open(file, "r").read())

for i in range(len(f)): #turning all non letter characters to spaces to be removed later
    if not f[i].isalpha():
        f[i] = " "

f = "".join(f).split() #f contains now only words


w = [0 for i in range(20)] #w[i] contains the amount of words the have i amount of letters(needs to be at least 19(for later))
wl = 20 #lenght of w(or the lenght of the longest word found if its above 18)

for i in f:
    x = len(i)-1
    
    if x + 1 > wl: #allows w to hold data for longer words(The longest word's lenght is not given)
        for j in range(x-wl+1): #gives w counters for all word lenghts up to x
            w.append(0)
        wl = x + 1
        
    w[x] += 1


def show_values(x, i):
    if x == 1:
        msg = "Υπάρχει μία λέξη "
    elif x > 1:
        msg = "Υπάρχουν " + str(x) + " λέξεις "

    if i == 1:
        msg += "του ενώς γράμματος"
    else:
        msg += "των " + str(i) + " γραμμάτων"

    print(msg)


for i in range(20):
    if w[i]-w[19-i] > 0:
        show_values(w[i]-w[19-i], i+1)
        
for i in range(20, len(w)): #in case there are words longer than 19 characters(no need to cancel out anything here)
    if w[i] > 0:
        show_values(w[i], i+1)

cmd_wont_close = input()
