import pandas as pd
import util
from sklearn import tree, model_selection

train = pd.read_csv("train.csv")
testD = pd.read_csv("test.csv")
util.data_cleanup(train)
util.data_cleanup(testD)

target = train["Survived"].values

feature_names = ["Sex","Age","Embarked","Pclass","Parch","SibSp"]
features = train[feature_names].values
featuresT = testD[feature_names].values

decision_tree = tree.DecisionTreeClassifier(random_state = 1, max_depth = 6, min_samples_split = 2)
decision_ = decision_tree.fit(features,target)
resultP = decision_.predict(featuresT)

print (decision_.score(features,target))

scores = model_selection.cross_val_score(decision_, features, target, scoring='accuracy', cv = 50)
print(scores)
print(scores.mean())
