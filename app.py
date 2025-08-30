from stack import Stack
from database import Database
from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html') #if it is a get method, startup the form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        my_database.add_user(username, password)

if __name__ == '__main__':
    my_database = Database()
    app.run(host='0.0.0.0',debug=True)    #turn to false once you actually make the application (0.0.0.0 allows you to do both local and global through the network)
    my_database.add_user('Brandon', 'password123')
    print(my_database.data)
    print(my_database.get_password())
    print(my_database.get_username())