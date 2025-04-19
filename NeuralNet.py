import random 
import math
import Graphs

G=Graphs()
G=MakeNet(16,2,3)

"""

oldProduct=100000000
rand=0.0
index=[0,2]
num=100000
for y in range(1,num):
    #chooses what to change it by
    rand=random.gauss(0,1/math.log(y+1))
    #chooses which edge to change
    index=[random.randint(0,5),random.randint(2,4)]
    #makes the change
    Edges[index[0]][index[1]]=Edges[index[0]][index[1]]+rand
    #computes the output for each of the good data points and updates the product accordingly
    for x in GoodData:
        Vertecies[0]=x[0]/(x[0]+x[1])
        Vertecies[1]=x[1]/(x[0]+x[1])
        run(Edges, Vertecies)
        product=product*(1+(out(Vertecies)-1)**2)
        Vertecies=[0,0,0,0,0]
    #computes the output for the bad data
    for x in BadData:
        Vertecies[0]=x[0]/(x[0]+x[1])
        Vertecies[1]=x[1]/(x[0]+x[1])
        run(Edges, Vertecies)
        product=product*(1+(out(Vertecies))**2)
        Vertecies=[0,0,0,0,0]
    #Chooses which set of parameters to use
    if(product>=oldProduct):
        Edges[index[0]][index[1]]=Edges[index[0]][index[1]]-rand
    else:
        oldProduct=product
        print(oldProduct,y)
    #Resets the product. Rinse, wash, repeat
    if(product==1):
        break
    product=1

print(Edges)


Vertecies[0]=.2/.7
Vertecies[1]=.5/.7
run(Edges,Vertecies)
print(out(Vertecies))
Vertecies=[0,0,0,0,0]

for x in GoodData:
    Vertecies[0]=x[0]/(x[0]+x[1])
    Vertecies[1]=x[1]/(x[0]+x[1])
    run(Edges, Vertecies)
    print(out(Vertecies))
    Vertecies=[0,0,0,0,0]
for x in BadData:
    Vertecies[0]=x[0]/(x[0]+x[1])
    Vertecies[1]=x[1]/(x[0]+x[1])
    run(Edges, Vertecies)
    print(out(Vertecies))
    Vertecies=[0,0,0,0,0]

"""