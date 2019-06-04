from sklearn.externals import joblib

clf  = joblib.load('sk.pkl') 
print clf.predict([['3', '1', '4', 2.0, 0.0, '2', 0.0, 0.0, 1.0]])

# import pickle
# print(pickle.format_version)
# filename = '../model/sk.pkl'
# loaded_model = pickle.load(open(filename, 'rb'))
# print(loaded_model.predict([['3', '0', '1', '2', '0', '2', '0', '0', '1']]))
# print(loaded_model.predict([[ '3', '1', '1', '0', '1', '1', '6', '774', '16' ]]))