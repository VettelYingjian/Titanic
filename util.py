def data_cleanup(data):
	data["Fare"] = data["Fare"].fillna(data["Fare"].dropna().median())
	data["Age"] = data["Age"].fillna(data["Age"].dropna().median())

	data.loc[data["Sex"] == "male", "Sex"] = 0
	data.loc[data["Sex"] == "female", "Sex"] = 1

	data["Embarked"] = data["Embarked"].fillna("S")

	data.loc[data["Embarked"] == "S", "Embarked"] = 0
	data.loc[data["Embarked"] == "C", "Embarked"] = 1
	data.loc[data["Embarked"] == "Q", "Embarked"] = 2

def data_restore(data):
	data.loc[data["Sex"] == 0, "Sex"] = "male"
	data.loc[data["Sex"] == 1, "Sex"] = "female"

	data.loc[data["Embarked"] == 0, "Embarked"] = "S"
	data.loc[data["Embarked"] == 1, "Embarked"] = "C"
	data.loc[data["Embarked"] == 2, "Embarked"] = "Q"


