import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")
fig =  plt.figure(figsize=(18,6))

plt.subplot2grid((2,3),(0,0))
df.Survived.value_counts(normalize=True).plot(kind="bar", alpha=0.5)
plt.title("Survived")

plt.subplot2grid((2,3),(0,1))
plt.scatter(df.Survived, df.Age, alpha=0.5)
plt.title("Age wrt Survived")

plt.subplot2grid((2,3),(1,0),colspan=2)
for x in [1,2,3]:
	df.Age[df.Pclass == x].plot(kind="kde")
	plt.title("Class")



plt.show()
print (df.shape)
print (df.count())