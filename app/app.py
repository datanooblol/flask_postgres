from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.secret_key = "hello"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///"
db = SQLAlchemy(app)



@app.route('/')
def index():
    return "<h1>Hello World! Aha</h1>"


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=80)