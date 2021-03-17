from flask import Flask, render_template, request, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from Predictor import makePrediction

app = Flask(__name__)

@app.route("/")
@app.route("/getPrediction", methods = ["GET", "POST"])
def getPrediction():
	if request.method == "POST":
		pregnant = request.form["pregnant"]
		glucose = request.form["glucose"]
		bp = request.form["bp"]
		skin = request.form["skin"]
		insulin = request.form["insulin"]
		bmi = request.form["bmi"]
		pedigree = request.form["pedigree"]
		age =  request.form["age"]
		valuePredicted = makePrediction(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age)

		hasDiabetesPr = valuePredicted['result'][0][0]
		hasNotDiabetesPr = valuePredicted['result'][0][0]
		return str(valuePredicted)
	return "You should use POST to get a Prediction"

@app.route("/validateResponse", methods = ["GET", "POST"])
def validateResponse():
	if request.method == "POST":
		pregnant = request.form["pregnant"]
		glucose = request.form["glucose"]
		bp = request.form["bp"]
		skin = request.form["skin"]
		insulin = request.form["insulin"]
		bmi = request.form["bmi"]
		pedigree = request.form["pedigree"]
		years =  request.form["years"]
		label = request.form["label"]
		return pregnant
	return "You should use POST to refit the model"

app.debug = True
app.run(host='0.0.0.0', port=5000)

# if __name__ == '__main__':
# 	app.debug = True
# 	app.run(host='0.0.0.0', port=5000)