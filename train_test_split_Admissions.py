import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('admission_ML.csv')

# Start build on Linear regression model

df.columns

X = df[['GRE Score', 'TOEFL Score', 'University Rating',
       'CGPA', 'Research']]

y = df['A']


# train and split data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state=101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

# print(lm.intercept_)
lm.coef_

X_train.columns

cdf = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])

# PREDICTIONS FROM TEST SET

predictions = lm.predict(X_test)



plt.scatter(y_test,predictions,color='b')
plt.xlabel("Y Test")
plt.ylabel("Predictions")
plt.show()




d = sns.distplot((y_test-predictions))

axes = plt.gca()
axes.set_xlim([-.2,0.2])
plt.title("Residual Distribution - Prediction")
axes.set_xlabel("Residual Error")
axes.set_ylabel("Number of Successes")





from sklearn import metrics

m1 = metrics.mean_absolute_error(y_test,predictions)

m2 = metrics.mean_squared_error(y_test,predictions)

m3 = np.sqrt(metrics.mean_squared_error(y_test,predictions))

print(m1)
print(m2)
print(m3)
