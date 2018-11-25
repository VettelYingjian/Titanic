import pandas as pd
import util
from sklearn import linear_model,preprocessing

train = pd.read_csv("train.csv")
util.data_cleanup(train)

target = train["Survived"].values
feature_names = ["Sex","Age","Embarked","Pclass","Parch","SibSp"]
features = train[feature_names].values

classifier = linear_model.LogisticRegression()
classifier_ = classifier.fit(features, target)

print (train.shape)
print (train.count())
print(classifier_.score(features, target))

poly = preprocessing.PolynomialFeatures(degree=3)
poly_features = poly.fit_transform(features)

classifier_ = classifier.fit(poly_features, target)
print(classifier_.score(poly_features, target))


