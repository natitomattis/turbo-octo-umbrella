from sklearn.externals import joblib

clf  = joblib.load('model/sk.pkl') 
print(clf.predict([['3', '1', '4', 2.0, 0.0, '2', 0.0, 0.0, 1.0]]))