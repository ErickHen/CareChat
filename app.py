import requests 
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def main():
    data = request.get_jason(silent = True)

    intentName = data['queryResult']['intent']['displayName']
    nome = data['queryResult']['parameters']['nome']
    idade = data['queryResult']['parameters']['idade']
    telefone = data['queryResult']['parameters']['telefone']

    if intentName == "IntentTest":
        data["fulfillmentText"] = {"Ok Sr(a) {nome}, {idade} anos, {telefone}."}

        return jsonify(data)

    if __name__ == "__main__":
        app.debug = False
        app.run