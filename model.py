from db import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import pickle
from random import randint


def train_AggToGrade ():
	model = LogisticRegression ()
	data, grade = selectCourse()
	
	x_train, x_test, y_train, y_test = train_test_split(data, grade, test_size=0.2, random_state=randint(0,9))
	model.fit(x_train, y_train)

	pickle.dump(model, open('Models/AggToGrade.sav', 'wb'))

	return model.score(x_test, y_test)

def predict_AggToGrade (avg, agg):
	model = pickle.load(open("Models/AggToGrade.sav", 'rb'))

	return model.classes_, model.predict_proba([(agg - avg, agg) ])[0]

def train_SemiToAgg (n):
	model = LinearRegression ()

	data, agg = selectPartialAgg (n)

	x_train, x_test, y_train, y_test = train_test_split(data, agg, test_size=0.2, random_state=randint(0,9))
	model.fit(x_train, y_train)

	pickle.dump(model, open('Models/SemiToAgg_'+str(n)+'.sav', 'wb'))

	return model.score(x_test, y_test)


def predict_SemiToAgg (mine, avg, n):
	model = pickle.load(open('Models/SemiToAgg_'+str(n)+'.sav', 'rb'))

	return model.predict([(mine, avg) ])


def getCourseGradeTable (user, course, n):
	mine, avg = selectUserCourseMarks(user, course, n)
	myAgg = predict_SemiToAgg(mine, avg, n)[0]
	avgAgg = predict_SemiToAgg(avg, avg, n)[0]

	grade, result = predict_AggToGrade(avgAgg, myAgg)
	for g, r in zip(grade, list(result)):
		print(g, round(r*100,1))