# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# create the application object
app = Flask(__name__)

app.secret_key = 'python'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'mysqlroot'
app.config['MYSQL_PASSWORD'] = 'anjali@97'
app.config['MYSQL_DB'] = 'loginapp'

# Intialize MySQL
mysql = MySQL(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return redirect(url_for('login'))  # return login page

@app.route('/welcome')
def welcome():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from categories")
    data = cursor.fetchall()
    return render_template('categories.html',rows=data)  # render a template

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'password' in request.form and 'cpassword' in request.form and 'email' in request.form  and 'phone' in request.form:
        
        # Create variables for easy access
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
        phone = request.form['phone']
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        # If account exists show error and validation checks
        if user:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif password != cpassword:
            msg = 'Passwords do not match' 
        elif not firstname or not lastname  or not password or not cpassword or not email or not phone:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s, %s)', (firstname, lastname, password, email, phone))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
        # Fetch one record and return result
        user = cursor.fetchone()

        if user:
    # Create session data, we can access this data in other routes
            session['loggedin'] = True
            
            # Redirect to home page
            return redirect(url_for('welcome'))
        else:
            # Account doesnt exist or username/password incorrect
            error = 'Incorrect username/password!'
           
    return render_template('login2.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
