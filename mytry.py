import kMeans
import numpy as np
# dataMat3 = np.mat(kMeans.loadDataSet('testSet2.txt'))
# centList, myNewAssments = kMeans.biKmeans(dataMat3,3)

geoResults = kMeans.geoGrab("1 VA Center","Augusta, ME")
kMeans.massPlaceFind('portlandClubs.txt')

# kMeans.clusterClubs(5)