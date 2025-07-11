from flask import Flask, render_template, jsonify
import mysql.connector
from mysql.connector import Error
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/dasboard_pedidos')
def dasboard_pedidos():
    return render_template('dasboard_pedidos.html')




if __name__ == '__main__':
    app.run(debug=True)


