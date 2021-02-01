app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost/bookexample'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost:5433/bookexample'

FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from flask import Flask

app = Flask(__name__)  # create a flask app named app


@app.route("/")
def home():
    return '''My name is Ogochukwu Ifesemen. This is my CA2 work.
      My GitHub URL is https://github.com/Ogoife/myISM209CA2.git'''
    # In the return statement above, Use your own name and GitHub URL


if __name__ == "__main__":
    app.run(port=5005)

    from flask import Flask, render_template

    app = Flask(__name__)


@app.route("/")


def home():
    return render_template('home.html', title="Home")


@app.route("/products-and-services/")
def products_and_services():
    return render_template('products-and-services.html', title="Products and Services")


@app.route("/about-us/")
def about_us():
    return render_template('about-us.html', title="About Us")


if __name__ == "__main__":
    app.run(
        port=5001)  # here we are using a different port so as not to conflict with that allocated to our helloworld.py
