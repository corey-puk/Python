import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


customers = pd.read_csv('Ecommerce Customers')
customers.head()

customers.describe()

customers.info()



#sns.jointplot(data=customers, x='Time on Website',y='Yearly Amount Spent')

#sns.jointplot(data=customers, x='Yearly Amount Spent', y='Time on App')



#sns.lmplot(x='Length of Membership', y='Yearly Amount Spent',data=customers)

customers.columns


y = customers['Yearly Amount Spent']

X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']]



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)


from sklearn.linear_model import LinearRegression

lm = LinearRegression()


lm.fit(X_train,y_train)



lm.coef_



predictions = lm.predict(X_test)


plt.scatter(y_test, predictions)
plt.xlabel('Y Test (True Values)')
plt.ylabel('Predicted Values')


#from sklearn import metrics

#print('MAE', metrics.mean_absolute_error(y_test,predictions))

#print('MSE', metrics.mean_squared_error(y_test,predictions))

#print('RMSE', np.sqrt(metrics.mean_squared_error(y_test,predictions)))

#metrics.explained_variance_score(y_test,predictions)
