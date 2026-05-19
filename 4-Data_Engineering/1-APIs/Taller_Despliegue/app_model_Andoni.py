from flask import Flask, request, jsonify

# creamos la instancia de la aplicación Flask
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def hello():
    return "Bienvenido a mi API del modelo advertising"


@app.route("/api/v1/predict", methods=["GET"])
def predict():

    # cargamos el modelo desde disco en cada petición
    # así si fue reentrenado, la siguiente predicción ya usa la versión nueva
    model = pickle.load(open('ad_model.pkl', 'rb'))

    # leemos los parámetros del query string (?tv=...&radio=...&newspaper=...)
    # request.args.get devuelve None si el parámetro no viene en la URL
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    print(tv, radio, newspaper)
    print(type(tv))

    if tv is None or radio is None or newspaper is None:
        return "Args empty, the data are not enough to predict"
    else:
        # construimos un DataFrame con los nombres de columna exactos con los que se entrenó el modelo
        # si pasáramos una lista plana [[tv, radio, newspaper]], sklearn lanzaría un warning
        # porque el modelo fue entrenado con un DataFrame con nombres de columna y espera lo mismo
        input_data = pd.DataFrame([[float(tv), float(radio), float(newspaper)]],
                                   columns=['TV', 'radio', 'newspaper'])
        prediction = model.predict(input_data)

    # jsonify convierte el resultado a JSON, formato estándar de respuesta en APIs
    return jsonify({'predictions': prediction[0]})

import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
import os

@app.route("/api/v1/retrain/", methods=["GET"])
def retrain():

    # comprobamos si existe el archivo con datos nuevos antes de hacer nada
    if os.path.exists("data/Advertising_new.csv"):
        data = pd.read_csv('data/Advertising_new.csv')

        X_train, X_test, y_train, y_test = train_test_split(
            data.drop(columns=['sales']),
            data['sales'],
            test_size=0.20,
            random_state=42
        )

        # entrenamos y evaluamos sobre el conjunto de test
        model = Lasso(alpha=6000)
        model.fit(X_train, y_train)
        rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
        mape = mean_absolute_percentage_error(y_test, model.predict(X_test))

        # reentrenamos con el 100% de los datos para maximizar la información antes de guardar
        model.fit(data.drop(columns=['sales']), data['sales'])

        # sobreescribimos el pkl — a partir de aquí /predict usará este modelo actualizado
        pickle.dump(model, open('ad_model.pkl', 'wb'))

        return f"Model retrained. New evaluation metric RMSE: {str(rmse)}, MAPE: {str(mape)}"
    else:
        return "<h2>New data for retrain NOT FOUND. Nothing done!</h2>"

app.run()

