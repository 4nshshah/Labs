from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

data = pd.read_csv("../datasets/knn.csv")
X = data.iloc[:,:2]
y = data.iloc[:,2:]
y = np.array(y)
def convert(x):
    if x=='Good':
        return 1
    return 0
y = list(map(convert,y))
data["Classification"] = y

#Using Minkowski
neigh = KNeighborsClassifier(n_neighbors=3,p=3, metric='minkowski')
neigh.fit(X,y)

print("Good" if neigh.predict([[3,7]]) else "Bad")

#Using Eucildean
neigh = KNeighborsClassifier(n_neighbors=3,p=2, metric='euclidean')
neigh.fit(X,y)

print("Good" if neigh.predict([[3,7]]) else "Bad")

#Using Manhattan Distance
neigh = KNeighborsClassifier(n_neighbors=3,p=1, metric='manhattan')
neigh.fit(X,y)

print("Good" if neigh.predict([[3,7]]) else "Bad")


####################################################################################################################################################################

import pandas as pd
import numpy as np

def euclidean(x1,y1,x,y):
    return ((x1-x)**2 + (y1-y)**2)**(1/2)

def manhattan(x1,y1,x,y):
    return abs(x1-x) + abs(y1-y)

def minkowski(x1,y1,x,y,p):
    return ((abs(x1-x))**p + (abs(y1-y))**p)**(1/p)

data = pd.read_csv("../datasets/knn.csv")

c1x,c1y,c2x,c2y = 7,7,3,4 
data["Distance c1"] = [0]*len(data)
data["Distance c2"] = [0]*len(data)

#Using Eucildean
clusters = []
flag = False
while(flag == False):
    for i in range(len(data)):
       # data.iloc[i:i+1,3:4] = euclidian(data.iloc[i:i+1,0:1],data.iloc[i:i+1,1:2],c1x,c1y)
        data.iloc[i:i+1,4:] = euclidean(data.iloc[i:i+1,0:1],data.iloc[i:i+1,0:1],c2x,c2y)
    break
    
data       