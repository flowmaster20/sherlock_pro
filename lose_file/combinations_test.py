tab = []
for i in range(5**5):
    a = str(int(i/1)%5)
    b = str(int(i/2)%5)
    c = str(int(i/3)%5)
    d = str(int(i/4)%5)
    e = str(int(i/5)%5)

    data = a+b+c+d+e
    print(data)
    tab.append(data)
tab = set(tab)
print (5**5,len(tab),len(tab)/5**5)


for 
