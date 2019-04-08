import cv2
import numpy as np
from sklearn.cluster import KMeans
def find_histogram(clt):
      
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    hist,_ = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()
    
    return hist
img = cv2.imread("notH_1.jpg") #change filename as you want
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
clt = KMeans(n_clusters=5) #cluster number
clt.fit(img)
hist = find_histogram(clt)
print(hist)
print("                           ")
print(clt.cluster_centers_)
print("                           ")
F_dms = [x for _,x in sorted(zip(hist,clt.cluster_centers_))]
F_dms.reverse()    
print(F_dms)
print("                           ")
list_hex = []
for i in F_dms:
     list_hex.append('#%02x%02x%02x' % tuple([int(j) for j in i]))
     #list_rgbs.append(tuple(i))
print("Hex codes are: ", list_hex )
print("                           ")

