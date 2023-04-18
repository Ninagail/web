# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route ("/")
def index():
    return render_template('Site.html')

@app.route ("/coucou")
def Coucou():
    return "<p>coucou<p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

