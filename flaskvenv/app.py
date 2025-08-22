from flask import Flask, render_template, request
import sqlite3
import os

# Create a Flask app instance
app = Flask(__name__)

# Database setup
DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                terms TEXT NOT NULL
            )
        ''')
        conn.commit()

# Home page route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')
        terms = 'checked' if request.form.get('terms') else 'not checked'

        # Insert into database
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO users (email, password, terms) VALUES (?, ?, ?)", (email, password, terms))
            conn.commit()

        return f"""
            <h1>Form Submitted!</h1>
            <p>Email: {email}</p>
            <p>Password: {password}</p>
            <p>Terms: {terms}</p>
        """

    return render_template('home.html')

@app.route('/users')
def users():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    # Return as simple HTML
    return '<br>'.join(str(user) for user in users)

# Initialize database before first request
@app.before_request
def initialize():
    init_db()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
