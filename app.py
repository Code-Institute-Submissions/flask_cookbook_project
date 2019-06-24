from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# Homepage route
@app.route('/')
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
