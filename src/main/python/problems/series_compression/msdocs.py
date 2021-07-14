l = [1,2,3,5,6,8,10,11,12]
l_of_l = []
n=[]
for i in range(len(l)):
    if l[i] == l[i-1] + 1:
        n.append(l[i])
        #print(n)
    else:
        l_of_l.append(n)
        n = [l[i]]
l_of_l.append(n)
final = []

for i in l_of_l:
    if len(i) != 0:
        final.append(f"{i[0]}-{i[-1]}")

print(final)
