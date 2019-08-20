import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


from sklearn.datasets import load_breast_cancer


cancer = load_breast_cancer()

#PCA helps to find the MOST IMPORTANT variables
#30 variables = 30 Dimensions
#Can't visualise beyond 3D-4D


df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])


from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()


scaler.fit(df)


scaled_data = scaler.transform(df)



# PCA

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)



# Reduce to 2 rows of data across 30 variables?


plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
