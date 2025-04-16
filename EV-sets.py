import random
import math

GoodData=[[.1,.2],[.2,.4],[.3,.6],[.4,.8],[.5,1]]
BadData=[[1,1],[1,0],[0,1],[.2,.1],[.4,.4],[.7,.9],[.4,0],[.8,.8],[.1,.6],[0,.5],[.1,.4]]

Vertecies=[0.0,0.0,0.0,0.0,0.0]
Edges=[[0,2,0,0,0],[0,3,0,0,0],[1,2,0,0,0],[1,3,0,0,0],[2,4,0,0,0],[3,4,0,0,0]]

def run(Edges,Vertecies):
    for x in Edges:
        Vertecies[x[1]]=Vertecies[x[1]]+Vertecies[x[0]]*x[2]+x[3]+Vertecies[x[0]]*x[4]*Vertecies[x[0]]
def out(Vertecies):
    if(Vertecies[len(Vertecies)-1]<0):
        return 0
    elif(Vertecies[len(Vertecies)-1]>1):
        return 1
    return Vertecies[len(Vertecies)-1]



product=1.0
oldProduct=100000000
rand=0.0
index=[0,2]
num=100000
for y in range(1,num):
    rand=random.uniform(-.002,.002)
    index=[random.randint(0,5),random.randint(2,4)]
    Edges[index[0]][index[1]]=Edges[index[0]][index[1]]+rand
    for x in GoodData:
        Vertecies[0]=x[0]/(x[0]+x[1])
        Vertecies[1]=x[1]/(x[0]+x[1])
        run(Edges, Vertecies)
        product=product*(1+(out(Vertecies)-1)**2)
        Vertecies=[0,0,0,0,0]
    for x in BadData:
        Vertecies[0]=x[0]/(x[0]+x[1])
        Vertecies[1]=x[1]/(x[0]+x[1])
        run(Edges, Vertecies)
        product=product*(1+(out(Vertecies))**2)
        Vertecies=[0,0,0,0,0]
    if(product>=oldProduct):
        Edges[index[0]][index[1]]=Edges[index[0]][index[1]]-rand
    else:
        oldProduct=product
        #print(oldProduct)
    product=1

print(oldProduct)
if(oldProduct<2):
    print(Edges)




Best=[[0, 2, -0.5782076203333077, -1.0060774083883612, 2.391490562724542], [0, 3, 0.9010781814510492, 0.6104538631788062, 2.225007867837574], [1, 2, -1.0579846563358342, -0.9963534106227614, 1.168365238047718], [1, 3, 0.5804452353533358, 0.6885457621529785, 1.7274284961122335], [2, 4, -1.981140797800587, -0.26309250389478217, 2.0558374109315505], [3, 4, -0.9048346740791873, -0.3231119768745551, -1.0119694373361623]]

Manual=[[0,2,1,0,0],[0,3,0,0,0],[1,2,-1,0,0],[1,3,0,0,0],[2,4,0,1,-100],[3,4,0,0,0]]



Vertecies[0]=.2/.7
Vertecies[1]=.5/.7
run(Best,Vertecies)
print(out(Vertecies))
Vertecies=[0,0,0,0,0]

for x in GoodData:
    Vertecies[0]=x[0]/(x[0]+x[1])
    Vertecies[1]=x[1]/(x[0]+x[1])
    run(Best, Vertecies)
    print(out(Vertecies))
    Vertecies=[0,0,0,0,0]
for x in BadData:
    Vertecies[0]=x[0]/(x[0]+x[1])
    Vertecies[1]=x[1]/(x[0]+x[1])
    run(Best, Vertecies)
    print(out(Vertecies))
    Vertecies=[0,0,0,0,0]