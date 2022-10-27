from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(35), nullable=False)
    lastname = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Author: {self.firstname}>'


@app.route('/')
def index():
    authors = Author.query.all()
    return render_template("index.html", authors=authors)


@app.route('/<int:author_id>')
def author(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('author.html', author=author)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']

    return render_template("create.html")


if __name__ == '__main__':
    app.run(debug=True)
