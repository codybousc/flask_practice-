from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3

app = Flask(__name__)

app.database = "sample.db"

@app.route('/')
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials."
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)
