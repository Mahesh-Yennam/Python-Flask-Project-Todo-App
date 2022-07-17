from flask import *
from db import *

app = Flask(__name__)

@app.route('/')
def home():
    todos = selecttodo()
    return render_template('home.html', todos=todos)

@app.route('/addtodo', methods=['post'])
def addtodo():
    title = request.form['title']
    body = request.form['body']
    t=(title,body)
    inserttodo(t)
    return redirect('/')

@app.route('/edit/<id>', methods=['get'])
def edit(id):
    data=edittodo(id)
    return render_template('edit.html', todo=data)

@app.route('/edittodo/<id>', methods=['post'])
def editnow(id):
    title = request.form['title']
    body = request.form['body']
    updatetodo(id,title,body)
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    deletetodo(id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)