from flask import Flask,render_template, request
import pickle

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
	integer_featutes = [int(x) for x in request.form.values()]
	model = pickle.load(open('hiring.pkl', 'rb'))
	result = model.predict([integer_featutes])
	result = round(result[0], 2)
	return render_template('index.html', predictions=f"The prediction of the salary is {result}")




if __name__ == "__main__":
	app.run(port=5000, debug=True)