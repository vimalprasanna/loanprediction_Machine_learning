import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;
from sklearn.model_selection import train_test_split;
from sklearn.metrics import confusion_matrix,classification_report;
df=pd.read_csv('loan_data.csv');
print(df.head());
df[df['credit.policy']==1]['fico'].hist(bins=35,alpha=0.6);
df[df['credit.policy']==0]['fico'].hist(bins=35,alpha=0.6);
plt.show();
df[df['not.fully.paid']==1]['fico'].hist(bins=35,alpha=0.6);
df[df['not.fully.paid']==0]['fico'].hist(bins=35,alpha=0.6);
plt.show();
sns.countplot(x='purpose',data=df,hue='not.fully.paid');
plt.show();
sns.jointplot(x='fico',y='int.rate',data=df);
plt.show();
sns.lmplot(x='fico',y='int.rate',data=df,hue='credit.policy');
plt.show();
from sklearn.model_selection import train_test_split;
from sklearn.metrics import confusion_matrix,classification_report;
final=pd.get_dummies(df,columns=['purpose']);
df=df.drop('purpose',axis=1);
df=pd.concat([final],axis=1);
X=df.drop('not.fully.paid',axis=1);
y=df['not.fully.paid'];
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101);
from sklearn.tree import DecisionTreeClassifier;
dt=DecisionTreeClassifier();
dt.fit(X_train,y_train);
dt_pred=dt.predict(X_test);
print(confusion_matrix(y_test,dt_pred));
print(classification_report(y_test,dt_pred));
from sklearn.ensemble import RandomForestClassifier;
rd=RandomForestClassifier(n_estimators=200);
rd.fit(X_train,y_train);
rd_pred=rd.predict(X_test);
print(confusion_matrix(y_test,rd_pred));
print(classification_report(y_test,rd_pred));