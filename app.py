from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []


@app.route('/')
def index():
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    todo_index = int(request.form.get('todo_index'))
    todos.pop(todo_index)
    return redirect('/')


app.debug = True
