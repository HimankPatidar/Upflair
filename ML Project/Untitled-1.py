# %%
import pandas as pd

# %%
df = pd.read_csv("./insurance.csv")
df.head()

# %%
df.columns = ['age','gender','bmi','children','smoker','region','EMI']
df.head()

# %%
df.info()

# %%
df.duplicated().sum()

# %%
df.isnull().sum()

# %%
filter_data = df[(df['gender']=="female") & (df['smoker']== 'yes') & (df['region'] == 'northwest')]
filter_data.shape

# %%
df['region'].value_counts()

# %%
smoky = df[(df['gender'] == "female") & (df['smoker'] == 'yes')]
smoky.head()

# %%
smoky['region'].value_counts()

# %%
df['children'].value_counts()

# %%
import seaborn as sns
import matplotlib as plt

# %%
sns.countplot(df['gender'])

# %%
sns.scatterplot(x='age', y="EMI", data=df, hue="smoker")

# %%
df['gender'] = df['gender'].map({'male' : 1, "female" : 0})

# %%
df['smoker'] = df['smoker'].map({'yes':1, 'no' : 0})

# %%
cleaned_data = pd.get_dummies(df).astype(int)
cleaned_data.head()

# %%
cleaned_data.to_csv('cleaned-insurence.csv', index=False)

# %%
x = cleaned_data.drop('EMI', axis=1)
y = cleaned_data[['EMI']]

# %%
from sklearn.model_selection import train_test_split

# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)


# %%
from sklearn.linear_model import LinearRegression

# %%
lr = LinearRegression()

# %%
lr.fit(x_train, y_train)

# %%

print("Training score : ",lr.score(x_train,y_train))
print("Testing score : ",lr.score(x_test,y_test))

# %%
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# %%
rdf = RandomForestRegressor()

# %%
rdf.fit(x_train, y_train)

# %%
print("Training score :", rdf.score(x_train, y_train))
print("Testing score :", rdf.score(x_test, y_test))

# %%
dt = DecisionTreeRegressor()


# %%
dt.fit(x_train, y_train)

# %%
print("Training Score : ", dt.score(x_train, y_train))
print("Testing Score : ", dt.score(x_test, y_test))

# %%
RandomForestRegressor()

# %%
print(RandomForestRegressor.__doc__)

# %%
import joblib

# %%
#joblib.dump(rdf, 'model.lb)
model = joblib.load("rfmodel.lb")

# %%
single_unseen_data_point = [[33	,1	,22	,0	,0	,	0	,1	,0	,0]]


# %%
model.predict(single_unseen_data_point)


