from stack import Stack
from database import Database
from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')


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
            return f"Invalid username or password", 401

@app.route('/regi', methods=['GET','POST'])
def register():
    if request.method == 'GET':  # When a GET request is sent, Flask renders the index.html file in templates
        return render_template('register.html') #if it is a get method, startup the form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        my_database.add_user(username, password)
        return f"User {username} added successfully! Current database: {my_database.data}"

if __name__ == '__main__':
    my_database = Database()
    app.run(host='0.0.0.0',debug=True)    #turn to false once you actually make the application (0.0.0.0 allows you to do both local and global through the network)
    print(my_database.data)
    print(my_database.get_password())
    print(my_database.get_username())