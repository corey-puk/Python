import seaborn as sns
import matplotlib.pyplot as plt


#Trying to find pattersn - not predict !


from sklearn.datasets import make_blobs


data = make_blobs(n_samples=200, n_features=2,centers=4,cluster_std=1.8,random_state=101)





#data



plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')



from sklearn.cluster import KMeans


kmeans = KMeans(n_clusters=4)


kmeans.fit(data[0])
