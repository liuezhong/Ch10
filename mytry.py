import kMeans
import numpy as np
dataMat = np.mat(kMeans.loadDataSet('testSet.txt'))
# print(dataMat)
# print(dataMat[:,0].min())
# print(kMeans.randCent(dataMat,2))
# print(kMeans.distEclud(dataMat[0],dataMat[1]))

myCentroids, clustAssing = kMeans.kMeans(dataMat,4)
print(myCentroids)
print("------------------")
# print(clustAssing)

# dataMat3 = np.mat(kMeans.loadDataSet('testSet2.txt'))
# centList, myNewAssments = kMeans.biKmeans(dataMat3,3)

geoResults = kMeans.geoGrab("1 VA Center","Augusta, ME")
kMeans.massPlaceFind('portlandClubs.txt')

# kMeans.clusterClubs(5)