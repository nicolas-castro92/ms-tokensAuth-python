import variable
from flask import Flask
import os
from flask import request
from jose import jwt

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/crear-token")
def crear():
    nombre = request.args.get("nombre")
    #print(os.environ.get("JWT_SECRET_KEY"))
    if nombre!=None:
        id_usuario = request.args.get("id_usuario")
        id_rol = request.args.get("id_rol")
        print(nombre, id_usuario, id_rol)
        print(type(nombre))
        try:
            secret_key = os.environ.get("JWT_SECRET_KEY")
            tk = jwt.encode({'nombre': nombre, 'id_usuario': id_usuario, 'rol': id_rol}, secret_key, algorithm='HS256')
            print(type(tk))
            print(tk)
            return tk
        except Exception as e:
            print(e.message)
            return "error"
    else:
        return "campos invalidos"

    return "terminado"

@app.route("/validar-token")
def validar():
    token = request.args.get("token")
    rol = request.args.get("rol")
    try:
        secret_key = os.environ.get("JWT_SECRET_KEY")
        token = jwt.decode(token, secret_key, algorithms=['HS256'])
        if token["rol"] == rol:
            return "OK"
        else:
            return "KO"
    except Exception as e:
        return "excepcion"


@app.route("/validar-session")
def validarSession():
    token = request.args.get("token")
    try:
        secret_key = os.environ.get("JWT_SECRET_KEY")
        token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return token
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(host="localhost", port=5001)




'''
>>> from jose import jwt
>>> token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')
u'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'

>>> jwt.decode(token, 'secret', algorithms=['HS256'])
{u'key': u'value'}
'''


'''

@app.route("/validar-token")
def validar():
    token = request.args.get("token")
    try:
        secret_key = os.environ.get("JWT_SECRET_KEY")
        jwt.decode(token, secret_key, algorithms=['HS256'])
        return "OK"
    except Exception as e:
        return "KO"


'''


'''
    try:
        secret_key = os.environ.get("JWT_SECRET_KEY")
        token = jwt.encode({'nombre': nombre, 'id': id_persona, 'rol': id_rol}, secret_key, algorithm='HS256')
        return {token}
    except Exception as e:
        return ""


'''
