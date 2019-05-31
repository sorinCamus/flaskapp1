from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

posts = [
    {
        'author': 'Bilc Sorin',
        'title': 'Blog Post One',
        'content': 'first post content',
        'date_posted': 'March 13, 2090'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post Two',
        'content': 'second post content',
        'date_posted': 'March 13, 2091'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration Page', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login Page', form=form)


if __name__ == '__main__':
    app.run(debug=True)
