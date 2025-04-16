import random

Gooddata=[[.5,.5],[1,1],[.1,.1],[.5,.55],[.85,.9]]
BadData=[[1,0],[0,1],[.3,.7],[.1,.3],[.7,1]]

class Node:
    def __init__(self,Nodes,nextas,nextbs):
        self.Nodes=Nodes
        self.a=nextas
        self.b=nextbs
    value=0.0
    def __str__(self):
        return f"{self.a},{self.b}"

class Value:
    def __init__(self,val):
        self.value=val

def zero(Nodes):
    for x in Nodes:
        x.value=0.0
def run(Nodes):
    for x in Nodes:
        for y in x:
            for z in range(0,len(y.Nodes)):
                y.Nodes[z].value=(y.a[z])*(y.value)+y.Nodes[z].value+y.b[z]


out=Node([],[],[])
h1=Node([out],[.5],[0.0])
h2=Node([out],[.5],[0.0])
n1=Node([h1,h2],[.5,.5],[0.0,0.0])
n2=Node([h1,h2],[.5,.5],[0.0,0.0])
StartingNodes=[n1,n2]
HiddenNodes=[h1,h2]
Nodes=[StartingNodes, HiddenNodes, [out]]
AllNodes=[n1,n2,h1,h2,out]
print(n2.Nodes)

product=1
oldProduct=2.8353685351562503
rand=0
index=0
ab=0
for y in range(0,100000):    
    rand=random.uniform(.2*(-.98**y),.2*(.98**y))
    index=random.randint(0,3)
    ab=random.randint(0,1)
    if(ab==0):
        AllNodes[index].a[0]=AllNodes[index].a[0]+rand
    else:
        AllNodes[index].b[0]=AllNodes[index].b[0]+rand
    for x in Gooddata:
        zero(AllNodes)
        n1.value=x[0]
        n2.value=x[1]
        run(Nodes)
        product=product*(1+(out.value-1)**2)
    for x in BadData:
        zero(AllNodes)
        n1.value=x[0]
        n2.value=x[1]
        run(Nodes)
        product=product*(1+(out.value-1)**2)
    if(product>oldProduct):
        if(ab==0):
            AllNodes[index].a[0]=AllNodes[index].a[0]-rand
        else:
            AllNodes[index].b[0]=AllNodes[index].b[0]-rand
    else:
        oldProduct=product
    product=1
print(oldProduct)
