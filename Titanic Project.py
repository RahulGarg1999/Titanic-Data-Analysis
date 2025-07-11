# Data Science Project(Youtube)

# https://www.youtube.com/watch?v=eN5dvVoGCyc&t=4586s

## Start

import pandas as pd

df = pd.read_csv("Titanic.csv")

2. Printing starting 10 rows and last 10 rows

df10 = df.head(10)
df10

df.tail(10)

3. Shape of the data

df.shape

4. Print all columns name

df.columns.tolist()

5. Find the data type of all the columns

df.dtypes

df.head()

type(df)

6. Print information and summary

df.describe()

df.info()

7. Count Survived and show on pie chart

var1 = df.Survived.value_counts()

import matplotlib.pyplot as plt

var1

plt.pie(var1, shadow=True, autopct="%0.2f%%", labels = ["Not-Survived", "Survived"], colors = ["r", 'g'])
plt.title("Survived and Not-Survived Passengers")
plt.show()

8. Find out how many female passengers had travelled in first class and show on pie chart

df.Sex.value_counts()

df_female = df[df.Sex == "female"]

var2 = df_female.Pclass.value_counts()
var2

plt.pie(var2, colors = ["#c85d46", "#467fc8", "#c8466b"], labels = ["3rd", "1st", "2nd"], autopct = "%0.01f %%", explode=(0, 0.1, 0))
plt.title("Female passengers travell with different classes")
plt.show()

9. Find out how many female passengers had Survived and her age <30, show on pie chart and bar graph

df_female[df_female.Age<30]

df_f_a = df[(df.Age<30) & (df.Sex=="female")]
var3 = df_f_a.Survived.value_counts()
var3

plt.pie(var3, shadow=True, autopct="%0.2f%%", labels = ["Survived", "Not-Survived"], colors = ["g", 'r'], explode = (0.1, 0))
plt.title("Female with her age<30")
plt.show()

10. Find out how many male passengers had Survived and his age >40, show on pie chart

df_m_a = df[(df.Age>40) & (df.Sex=="male")]
var4 = df_m_a.Survived.value_counts()
var4

plt.pie(var4, shadow=True, autopct="%0.2f%%", labels = ["Not-Survived", "Survived"], colors = ["r", 'g'], explode = (0, 0.1))
plt.title("Male with his age>40")
plt.show()

11. Show age with 20 bins

df.Age

import numpy as np

counts, bins, _ = plt.hist(df.Age, bins = 20, color = "yellow", edgecolor = "red", label = "Age bins")
bin_centers = (bins[:-1]+ bins[1:])/2
plt.plot(bin_centers, counts, marker = 'o', color="r", label = "Age Distribution")
plt.xticks(np.arange(0, 84, 4))
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

12. Show age frequency with survived and not survived (Histogram)

var5 = df[df.Survived == 1].Age
counts, bins, _ = plt.hist(var5, bins = 20, color = "yellow", edgecolor = "red", label = "Age bins")
bin_centers = (bins[:-1]+ bins[1:])/2
plt.plot(bin_centers, counts, marker = 'o', color="r", label = "Age Distribution")
plt.xticks(np.arange(0, 84, 4))
plt.title("Survived Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

var5 = df[df.Survived == 0].Age
counts, bins, _ = plt.hist(var5, bins = 20, color = "yellow", edgecolor = "red", label = "Age bins")
bin_centers = (bins[:-1]+ bins[1:])/2
plt.plot(bin_centers, counts, marker = 'o', color="r", label = "Age Distribution")
plt.xticks(np.arange(0, 84, 4))
plt.title("Not-Survived Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

13. Show Bar graph for Survived with male, female, class

s_df = df[df.Survived == 1]

s_df.Sex.value_counts()

s_df.Pclass.value_counts()

import seaborn as sns

sns.countplot(x = "Pclass", hue = "Sex", data = s_df)

14. How many passengers are travelled in different classes show in Bar graph

temp = df.Pclass.value_counts()
temp

value = list(temp)

data = dict(temp)
x = data.keys()
count = data.values()

count

import matplotlib.pyplot as plt

val = []
for i in x:
  if i ==1:
    val.append("1st Class")
  elif i==2:
    val.append("2nd Class")
  elif i==3:
    val.append("3rd Class")

x

val

plt.bar(val, count, color=["red", "green", "blue"])
plt.title("Passenger Class")
plt.xlabel("Classes")
plt.ylabel("Count of passengers")
plt.grid()
plt.show()

15. How many passengers are survived with class wise and show in Bar graph

sns.countplot(x = "Pclass", hue = "Survived", data = df)

16. Show Question-13 & Question-14 in subplot

sns.countplot(x = "Pclass", hue = "Sex", data = s_df)

fig, axs = plt.subplots(1,2, figsize=(10, 3))
sns.countplot(x = "Pclass", hue = "Sex", data = s_df, ax = axs[0])
axs[0].set_title("Survived passenger for gender and class")
axs[1].bar(val, count, color=["red", "green", "blue"])
axs[1].set_title("Passenger Class")
axs[1].set_xlabel("Classes")
axs[1].set_ylabel("Count of passengers")
axs[1].grid()
plt.show()

17. Show Bar graph for Survived with 3rd class male, 1st class female

df[(df.Pclass == 3) & (df.Sex == "male")].Survived.value_counts()

df[(df.Pclass == 3) & (df.Sex == "male")].Survived.value_counts().plot(kind = "bar", color= ["r", "g"])

df[(df.Pclass == 1) & (df.Sex == "female")].Survived.value_counts().plot(kind = "bar", color= ["g", "r"])

18. How many passengers are survived / not survived and they are 1st class female

df[(df.Pclass == 1) & (df.Sex == "female")].Survived.value_counts()

pd.crosstab(df["Pclass"], df["Sex"])

pd.crosstab(df["Pclass"], df["Sex"], margins= True)

Subplots

fig, axs = plt.subplots(2, 2, figsize = (10, 8))

var1 = df[(df.Pclass == 3) & (df.Sex == "male")].Survived.value_counts()
var1.plot(kind = "bar", color= ["r", "g"], ax = axs[0][0])
axs[0][0].set_title("3rd class Male Passengers")

var1 = df[(df.Pclass == 1) & (df.Sex == "female")].Survived.value_counts()
var1.plot(kind = "bar", color= ["g", "r"], ax = axs[0][1])
axs[0][1].set_title("1st class Female Passengers")

sns.countplot(x = "Pclass", hue = "Sex", data = df[(df.Survived == 1)], ax = axs[1,0])
axs[0][0].set_title("Passenger classes along with Sex")

var4 = df[(df.Sex == "male") & (df.Age>40)].Survived.value_counts()
axs[1][1].pie(var4, shadow=True, autopct="%0.2f%%", labels = ["Not-Survived", "Survived"], colors = ["r", 'g'], explode = (0, 0.1))
axs[1][1].set_title("Male with his age>40")

plt.show()

19.  Map the Sex column male=1, female =0

df.head()

df.Sex = df.Sex.map({"male":1, "female":0})

df

Label Encoder

df.Embarked.unique()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["Embarked"] = le.fit_transform(df["Embarked"])

df

20. Find Null values

df = pd.read_csv("Titanic.csv")

df.isnull().sum()

df.Age.isnull().sum()

df[df.Age.isnull()]

df.Age.describe()

df["Age"] = df.Age.fillna(28)

df

22. Drop unwanted columns

df.head()

cols = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

final_df = df[cols]

final_df.Sex = final_df.Sex.map({"male":1, "female":0})

final_df