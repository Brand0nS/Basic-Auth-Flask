from stack import Stack
from database import Database
from flask import Flask, request, render_template, redirect, url_for, flash


app = Flask(__name__, template_folder='templates')

app.secret_key = 'secretkey123'

@app.route('/')
def home():
    return redirect(url_for('index')) # redirects to the actual login page

@app.route('/login', methods=['GET','POST'])
def index():
    if request.method == 'GET':  # When a GET request is sent, Flask renders the index.html file in templates
        return render_template('index.html') #if it is a get method, startup the form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if my_database.verify_user(username,password):
            return f"Welcome {username} !"
        else: 
            flash("Invalid username or password.", "error")
            return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':  # When a GET request is sent, Flask renders the index.html file in templates
        return render_template('register.html') #if it is a get method, startup the form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        my_database.add_user(username, password)
        flash(f"User {username} added successfully! Current database: {my_database.data}", "success") 
        return redirect(url_for('index'))

if __name__ == '__main__':
    my_database = Database()
    app.run(host='0.0.0.0',debug=True)    #turn to false once you actually make the application (0.0.0.0 allows you to do both local and global through the network)
    print(my_database.data)
    print(my_database.get_password())
    print(my_database.get_username())