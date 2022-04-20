from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@192.168.0.2/students"
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "students"
    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String(40))
    lname=db.Column(db.String(40))
    pet=db.Column(db.String(40))

    def __init__(self, fname, lname, pet):
        self.fname=fname
        self.lname=lname
        self.pet=pet

@app.route('/')
def index():
    return "<h1>Hello World! Aha</h1>"

@app.route("/submit", methods=["GET","POST"])
def submit():
    student=Student(fname="oh",lname="my", pet="god")
    db.session.add(student)
    db.session.commit()

    studentResult = db.session.query(Student).filter(Student.id==1)
    for result in studentResult:
        print(result.fname)

    return f"{result.fname}:{result.lname}:{result.pet}"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=80)