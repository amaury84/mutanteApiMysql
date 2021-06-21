"""from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
"""

from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource, reqparse
import json

import mutante
from conectamysql import conectadb, consultadb, insertadb

app = Flask(__name__)
api = Api(app)
"""
@app.route('/', methods=['GET'])
def get():
    return {"mensaje":"** liga de magneto **"},200
"""
@app.route('/', methods=['GET'])
@app.route('/mutant', methods=['GET'])
def home():
    return render_template("index.html"),200

@app.route('/mutant', methods=['POST'])
def post():
    dna=request.data    
    dna = json.loads(dna)
    #tipo = type(dna["dna"])
    dnalist=dna["dna"]
    #return str(dnalist)

    if mutante.isAdn(dnalist):        
        if mutante.isMutant(dnalist):
            msj="HTTP 200-OK"
            insertadb(str(dnalist),True)
            return {"msj":msj},200
        else:
            msj="HTTP 403-FORBIDDEN"
            insertadb(str(dnalist),False)
            return {"msj":msj},403
    else:
        msj = "revisa la cadena de ADN, debe ser de dimesiones NxN y contener sólo elementos ACTG"
        return {"msj":msj},200
    
@app.route('/stats', methods=['GET','POST'])
def info():
    resultado = consultadb()
    return resultado
    
    
if __name__ == "__main__":
    app.run(debug=True)
