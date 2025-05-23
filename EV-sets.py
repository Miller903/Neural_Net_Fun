import random 
import math

#Outlining the data that I will use to train the model
GoodData=[[0.05,.1],[.1,.2],[.2,.4],[.3,.6],[.4,.8],[.5,1]]
BadData=[[1,1],[1,0],[0,1],[.2,.1],[.4,.4],[.7,.9],[.4,0],[.8,.8],[.1,.6],[0,.5],[.1,.4]]

#establishing the structure of the neural net. Drawn as a graph, there are two input vertecies fully connected to two hidden vertecies, which are both connected to an output vertex
Vertecies=[0.0,0.0,0.0,0.0,0.0]
Edges=[[0,2,0,0,0],[0,3,0,0,0],[1,2,0,0,0],[1,3,0,0,0],[2,4,0,0,0],[3,4,0,0,0]]
#the first 2 numbers denote which vertecies the edge connects, the last 3 numbers the quadratic function associated with the edge

#updates the entire graph once the inputs are entered
def run(Edges,Vertecies):
    for x in Edges:
        Vertecies[x[1]]=Vertecies[x[1]]+Vertecies[x[0]]*x[2]+x[3]+Vertecies[x[0]]*x[4]*Vertecies[x[0]]


#Reads the output vertex. This number will designate how likely a given data point is to belong to the set of good data. The good data should read all 1s, the bad data all 0s
def out(Vertecies):
    if(Vertecies[len(Vertecies)-1]<0):
        return 0
    elif(Vertecies[len(Vertecies)-1]>1):
        return 1
    return Vertecies[len(Vertecies)-1]


#Running the Markov chain
#I define a product over my training data of the absolute value of the difference between the actual output value and the expected output value
#The Markov chain randomly changes the edge parameters and computes the new product.
#If the new product is better, the new parameters are used.
product=1.0
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

"""

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