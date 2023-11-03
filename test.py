list = [[0,2],[0,3],[0,4],[0,5]]

for i in range(0,len(list)):
    if (i+1 < len(list)): 
        s = list[i+1]
    print(list[i], s)