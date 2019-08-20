import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

cancer.keys()


df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])


df_feat.head(2)




X = df_feat
y = cancer['target']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = 101)


from sklearn.svm import SVC

model = SVC()

model.fit(X_train,y_train)


predictions = model.predict(X_test)


from sklearn.metrics import classification_report, confusion_matrix


print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))



from model_selection import GridSearchCV
