import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")
fig =  plt.figure(figsize=(18,6))

plt.subplot2grid((3,3),(0,0))
df.Survived[df.Sex == "male"].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("Survived Male")

plt.subplot2grid((3,3),(0,1))
df.Survived[df.Sex == "female"].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("Survived Female")

plt.subplot2grid((3,3),(0,2))
df.Sex[df.Survived == 1].value_counts(normalize = True).plot(kind="bar", alpha = 0.5, color=["r","b"])
plt.title("Age wrt Survived")


plt.subplot2grid((3,3),(1,0),colspan=3)
for x in [1,2,3]:
	df.Survived[df.Pclass == x].plot(kind="kde")
plt.title("Class")


plt.subplot2grid((3,3),(2,0))
df.Survived[(df.Sex == "female") & (df.Pclass == 1)].value_counts(normalize=True).plot(kind="bar", alpha=0.5, color="r")
plt.title("Survived Female")


plt.subplot2grid((3,3),(2,1))
df.Survived[(df.Sex == "male") & (df.Pclass == 3)].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("Survived male")


plt.show()
print (df.shape)
print (df.count())
print (df.Survived[(df.Sex == "female") & (df.Pclass == 1)])