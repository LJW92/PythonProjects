from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[
        DataRequired(),
        Email(message="Invalid email address.")
    ])
    password = PasswordField(label='password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long.")
    ])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "some secret string"


bootstrap = Bootstrap5(app)
# Define a dictionary of valid credentials
valid_credentials = {
    'email': 'admin@email.com',
    'password': '12345678'
}


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        # Check if user provided credentials match the valid credentials
        if form.email.data == valid_credentials['email'] and form.password.data == valid_credentials['password']:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
