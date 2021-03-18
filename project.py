from flask import Flask, render_template, request, redirect, url_for
from Predictor import makePrediction, refit
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app = app, version="1.0", title="SlashMobility Predictor Program", description="Poject that returns if a patient has diabetes based on certain information")

name_space = api.namespace('api', description='Main Route to predict')

predictModel = api.model('Prediction Model', 
		  {'pregnant': fields.Integer(required = True, description="Number of times pregnant", help="pregnant cannot be blank."),
		  'glucose': fields.Integer(required = True, description="Plasma glucose concentration a 2 hours in an oral glucose tolerance test", help="glucose cannot be blank."),
		  'bp': fields.Integer(required = True, description="Diastolic blood pressure (mm Hg)", help="bp cannot be blank."),
		  'skin': fields.Integer(required = True, description="Triceps skin fold thickness (mm)", help="skin cannot be blank."),
		  'insulin': fields.Integer(required = True, description="2-Hour serum insulin (mu U/ml)", help="insulin cannot be blank."),
		  'bmi': fields.Integer(required = True, description="Body mass index (weight in kg/(height in m)^2)", help="pedigree cannot be blank."),
		  'pedigree': fields.Integer(required = True, description="Diabetes pedigree function", help="Name cannot be blank."),
		  'age': fields.Integer(required = True, description="Age (years)", help="age cannot be blank.")
		  })

validateModel = api.model('Validation Model', 
		  {'pregnant': fields.Integer(required = True, description="Number of times pregnant", help="pregnant cannot be blank."),
		  'glucose': fields.Integer(required = True, description="Plasma glucose concentration a 2 hours in an oral glucose tolerance test", help="glucose cannot be blank."),
		  'bp': fields.Integer(required = True, description="Diastolic blood pressure (mm Hg)", help="bp cannot be blank."),
		  'skin': fields.Integer(required = True, description="Triceps skin fold thickness (mm)", help="skin cannot be blank."),
		  'insulin': fields.Integer(required = True, description="2-Hour serum insulin (mu U/ml)", help="insulin cannot be blank."),
		  'bmi': fields.Integer(required = True, description="Body mass index (weight in kg/(height in m)^2)", help="bmi cannot be blank."),
		  'pedigree': fields.Integer(required = True, description="Diabetes pedigree function", help="pedigree cannot be blank."),
		  'age': fields.Integer(required = True, description="Age (years)", help="age cannot be blank."),
		  'label': fields.Integer(required = True, description="0: She has not diabetes, 1: She has diabetes", help="label cannot be blank.")
		  })

@name_space.route("/getPrediction")
class PredictorClass(Resource):

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })

	@api.expect(predictModel)

	def post(self):
		try:

			pregnant = request.json["pregnant"]
			glucose = request.json["glucose"]
			bp = request.json["bp"]
			skin = request.json["skin"]
			insulin = request.json["insulin"]
			bmi = request.json["bmi"]
			pedigree = request.json["pedigree"]
			age =  request.json["age"]

			valuePredicted = makePrediction(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age)

			hasDiabetesPr = valuePredicted['result'][0][1]
			hasNotDiabetesPr = valuePredicted['result'][0][0]
			return {
				"yes": hasDiabetesPr,
				"no": hasNotDiabetesPr
			}

		except KeyError as e:
			name_space.abort(500, e.__doc__, status="Could not make prediction, check proper fields", statusCode = "500")

		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not make prediction, check proper fields", statusCode = "400")

@name_space.route("/validatePrediction")
class ValidatorClass(Resource):

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })

	@api.expect(validateModel)

	def post(self):
		try:

			pregnant = request.json["pregnant"]
			glucose = request.json["glucose"]
			bp = request.json["bp"]
			skin = request.json["skin"]
			insulin = request.json["insulin"]
			bmi = request.json["bmi"]
			pedigree = request.json["pedigree"]
			age =  request.json["age"]
			label = json.form["label"]

			refit(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age, label)

			return {
				"message": "model refit successfully"
			}

		except KeyError as e:
			name_space.abort(500, e.__doc__, status="Could not make prediction, check proper fields", statusCode = "500")

		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not make prediction, check proper fields", statusCode = "400")



# @app.route("/getPrediction", methods = ["GET", "POST"])
# def getPrediction():
# 	if request.method == "POST":
# 		pregnant = request.form["pregnant"]
# 		glucose = request.form["glucose"]
# 		bp = request.form["bp"]
# 		skin = request.form["skin"]
# 		insulin = request.form["insulin"]
# 		bmi = request.form["bmi"]
# 		pedigree = request.form["pedigree"]
# 		age =  request.form["age"]
# 		valuePredicted = makePrediction(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age)

# 		hasDiabetesPr = valuePredicted['result'][0][0]
# 		hasNotDiabetesPr = valuePredicted['result'][0][0]
# 		return str(valuePredicted)
# 	return "You should use POST to get a Prediction, data in the body must be sent"

# @app.route("/validateResponse", methods = ["GET", "POST"])
# def validateResponse():
# 	if request.method == "POST":
# 		pregnant = request.form["pregnant"]
# 		glucose = request.form["glucose"]
# 		bp = request.form["bp"]
# 		skin = request.form["skin"]
# 		insulin = request.form["insulin"]
# 		bmi = request.form["bmi"]
# 		pedigree = request.form["pedigree"]
# 		age =  request.form["age"]
# 		label = request.form["label"]
# 		refit(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age, label)

# 		return "OK"
# 	return "You should use POST to refit the model, data in the body must be sent"

app.debug = True
app.run(host='0.0.0.0', port=5000)
