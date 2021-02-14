# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return redirect(url_for('login'))  # return login page

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/register')
def register():
    return render_template('register.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again later.'
        else:
            return redirect(url_for('welcome'))
            error = None
    return render_template('login2.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)