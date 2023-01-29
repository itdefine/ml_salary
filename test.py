import pickle


model = pickle.load(open('hiring.pkl', 'rb'))
print(model.predict([[1,2,3]]))