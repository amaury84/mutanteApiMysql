# mutanteApiMysql

_Esta api de prueba ha sido desarrollada en **Python** para resolver un reto de clasificaci贸n de ADN mutante y no mutante =)
los respectivos servicios POST se encuentran en_:

https://ligamagnetosql-f4vojxibla-uc.a.run.app/mutant

Para usar esta servicio, env铆a la cadena ADN en formato json usando un m茅todo POST. Ejemplo:
```
{
"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}
```
https://ligamagnetosql-f4vojxibla-uc.a.run.app/stats

Este servicio devuelve estad铆sticas en formato JSON. Ejepmlo:
```
{
"count_mutant_dna": 2, "count_human_dna": 0, "ratio": 1.0
}
```
## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._

### Pre-requisitos 馃搵
**Tener una versi贸n de Python instalada > 3.5**

**puedes crear la base de datos importanto el siguiente c贸digo en tu gestor favorito como PhpMyAdmin o MySQL WORKBENCH**

```
create database ligamagneto:
use ligamagneto;
create table usuarios(
    adn varchar(200) NOT NULL PRIMARY KEY,
    mutante bool NOT NULL
    );
```

### Instalaci贸n 馃敡

clona el proyecto en tu entorno virtual de Python

```
git clone https://github.com/amaury84/mutanteApiMysql
```

_corre los requerimientos para instalar todas las librerias y el framework_

```
pip install -r requerimientos.txt
```

_Una vez creada la base de datos y clonado el proyecto e instalado los requerimientos, puedes ejecutar el script pruebas.py
Se debe tener en cuenta que este desarrollo s贸lo almacena una cadena dna por registro_
```
python pruebas.py
```

## Ejecutando las pruebas 鈿欙笍

_Una vez creada la base de datos y clonado el proyecto e instalado los requerimientos, puedes ejecutar el script pruebas.py cambiando cada vez la cadena dna
Se debe tener en cuenta que este desarrollo s贸lo almacena una cadena dna por registro_

### Iniciando el script app.py para levantar la API de forma local 馃敥
```
python app.py
```

_Cuando se env铆a una cadena de ADN en formato JSON, hay dos m茅todos que verifican la cadena_

* _El primero, **mutante.isAdn(dna)** devuelve True si la cadena tiene una sintaxis correcta._
 _Cuando devuelve un False, retorna un JSON con un mensaje para verificar la sintaxis de la cadena ADN_

* _El segundo, **mutante.isMutant(dna)** devuelve True si la cadena pertenece a un mutante y la agrega a la base de datos._
_Cuando devuelve un False, agrega la cadena no mutante a la base de datos_
```
#c贸digo ejemplo del m茅todo app.py

from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource, reqparse
import json

import mutante
from conectamysql import conectadb, consultadb, insertadb

app = Flask(__name__)
api = Api(app)

@app.route('/mutant', methods=['POST'])
def post():
    dna=request.data    #Obtiene el JSON enviado por Postman o por prueba.py
    dna = json.loads(dna)
    #tipo = type(dna["dna"])
    dnalist=dna["dna"]
    #return str(dnalist)

    if mutante.isAdn(dnalist):        
        if mutante.isMutant(dnalist):
            msj="HTTP 200-OK"
            insertadb(str(dnalist),True) #Agrega un mutante a la base de datos
            return {"msj":msj},200
        else:
            msj="HTTP 403-FORBIDDEN"
            insertadb(str(dnalist),False) #Agrega una persona a la base de datos
            return {"msj":msj},403
    else:
        msj = "revisa la cadena de ADN, debe ser de dimesiones NxN y contener s贸lo elementos ACTG"
        return {"msj":msj},200
        
if __name__ == "__main__":
    app.run(debug=True)
```
### Enviando una cadena ADN en formato JSON 馃敥
```
import requests, json

dna = {
    "dna":["ATGCGA","CCGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    }
dna = json.dumps(dna) #transformar el dict a json

urllocal = "http://localhost:5000/mutant"
r = requests.post(urllocal ,data=dna)
print(r.json())
```
O si lo prefiere, puede utilizar [Postman](https://www.postman.com/)

Como respuesta, el servicio retorna un JSON dependiendo de la verificaci贸n
```
{
    "msj": "HTTP 200-OK"
}
```
```
{
    "msj": "HTTP 403-FORBIDDEN"
}
```
```
{
    "msj": "revisa la cadena de ADN, debe ser de dimesiones NxN y contener s贸lo elementos ACTG"
}
```

### Revisando el servicio /stats 馃敥
El m茅todo /stats se puede obtener por medio de un GET o un POST y est谩 incluido en el script app.py
```
@app.route('/stats', methods=['GET','POST'])
def info():
    resultado = consultadb()
    return resultado
```
para ejecutarlo, puede emplear el siguiente c贸digo de python o usar [Postman](https://www.postman.com/)
```
import requests, json

urllocal = "http://localhost:5000/stats"
r = requests.post(urllocal)
print(r.json())
```

## Despliegue en la nube Google Cloud 馃摝

Se ha creado una instancia Cloud Run y Sql en Google Cloud para su desplieque usando Python-Flask Python3.8

* Tener en cuenta que el sistema de Cloud Run emplea docker para crear la instancia, por lo cual se recomienda cambiar el contenido
del archivo requirements por el de requeriemientos y no editar el .dockerfile

* Instalar en el Cloud Run por medio de una terminal la libreria import pymysql.cursors empleada en el m茅todo conectamysql.py 
y editar en ese archivo la url p煤blica o privada asignada por el servicio SQL
```
#fragmento archivo conectamysql.py
import pymysql.cursors
import json

def conectadb():    
    # Connect to the database
    db = pymysql.connect(host='localhost', #cambiar localhost por la url de la instancia SQL
                         user='root',
                         password='',
                         database='ligamagneto',
                         cursorclass=pymysql.cursors.DictCursor)

    # prepare a cursor object using cursor() method
    return db,db.cursor()
```
* ejecute el siguiente comando en la terminal antes de hacer el deploy
```
pip3 install pymsql pymsql.cursors
```
* Edite el archivo app.py en las 煤ltimas lineas cambiando el if __name__=="__main"__ por este c贸digo
```
import os
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
```

## Construido con 馃洜锔?

* [Python-Flask](https://flask.palletsprojects.com/en/2.0.x/) - El framework web usado

## Autores 鉁掞笍

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Amaury M茅ndez** - *Trabajo Inicial* - [amaury84](https://github.com/amaury84)
