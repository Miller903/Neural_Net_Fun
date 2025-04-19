import math

#Edges store the function between the vertecies, characterized by a vector of floating points
class Edge:
    def __init__(self,node1,node2,parameters):
        self.node1=node1
        self.node2=node2
        self.parameters=parameters
    def run(self):
        #Assuming that the function is a polynomial with terms indexed 1,x,x^2,...
        for x in range(0,len(self.parameters)):
            self.node2.value=self.node2.value+self.parameters[x]*(self.node1.value**x)

#Not sure if I need a class for this, but whatever
class Node:
    def __init__(self,value):
        self.value=value

class Graph:
    def __init__(self,Nodes,Edges):
        self.Nodes=Nodes
        self.Edges=Edges
    def zero(self):
        for x in self.Nodes:
            x.value=0
    def run(self):
        for x in self.Edges:
            x.run()
    def set(self,nums):
        for x in range(0,len(nums)):
            self.Nodes[x].value=nums[x]

class Net(Graph):
    def __init__(self, numOfNodes,numOfPartitions, numOfParameters):
        self.numOfNodes=numOfNodes
        self.numOfPartitions=numOfPartitions
        self.numOfParameters=numOfParameters
        super().__init__([],[])
        self.Nodes=[0]*(numOfNodes*numOfPartitions+1)
        for x in range(0,numOfNodes*numOfPartitions+1):
            self.Nodes[x]=Node(0)
        self.Edges=[0]*(numOfNodes*numOfNodes*(numOfPartitions-1)+numOfNodes)
        for x in range(0,numOfPartitions-1):
            for y in range(0,numOfNodes):
                for z in range(0,numOfNodes):
                    self.Edges[x*numOfNodes*numOfNodes+y*numOfNodes+z]=Edge(self.Nodes[x*numOfNodes+y],self.Nodes[(x+1)*numOfNodes+z],([0]*numOfParameters))
                    for k in range(0,numOfParameters):
                        if(k==1 and y==z):
                            self.Edges[x*numOfNodes*numOfNodes+y*numOfNodes+z].parameters[k]=1
                        else:
                            self.Edges[x*numOfNodes*numOfNodes+y*numOfNodes+z].parameters[k]=0
        for x in range(0,numOfNodes):
            self.Edges[x+numOfNodes*numOfNodes*(numOfPartitions-1)]=Edge(self.Nodes[numOfNodes*(numOfPartitions-1)+x],self.Nodes[numOfNodes*numOfPartitions],([0]*numOfParameters))
            for k in range(0,numOfParameters):
                if(k==1):
                    self.Edges[x+numOfNodes*numOfNodes*(numOfPartitions-1)].parameters[k]=1
                else:
                    self.Edges[x+numOfNodes*numOfNodes*(numOfPartitions-1)].parameters[k]=0


    def run(self):
            super().run()


    def inputSet(self,nums):
        super().zero()
        for x in range(0,len(nums)):
            self.Nodes[x].value=nums[x]
            




G=Net(8,4,2)

print(G.Nodes[32].value)

G.inputSet([1]*8)
G.run()
print(G.Nodes[32].value)

"""

#testing that it works
one=Node(1)
two=Node(0)
E=Edge(one,two,[1])
G=Graph([one, two], [E])
G.run()
print(G.Nodes[1].value)
G.zero()
print(G.Nodes[0].value)
G.set([1,1])
G.run()
G.run()
print(G.Nodes[1].value)
"""