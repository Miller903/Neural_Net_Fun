import math

Gooddata=[[.5,.5],[1,1],[.1,.1]]
BadData=[[1,0],[0,1]]

def circle(vector):
    if(vector[1]==0):
        return 0
    return math.atan(vector[0]/vector[1])

def count(goodData,badData):
    return len(goodData)+len(badData)

def func(goodData,badData):
    A=[]
    b=[]
    for y in range(0,len(goodData)-1):
        b=[]
        for x in range(0,count(goodData,badData)-1):
            b.append(math.sin(x*circle(goodData[y])))
        A.append(b)
    for y in range(0,len(badData)):
        b=[]
        for x in range(0,count(goodData,badData)-1):
            b.append(math.sin(x*circle(badData[y])))
        A.append(b)
    print(A)

func(Gooddata,BadData)
