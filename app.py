from flask import Flask, render_template, request, redirect, url_for, session, flash
import tensorflow as tf
import numpy as np
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "4EF246C33859B457DF9CA73CD2626"

# Load the ML model
model_path = os.path.join("model", "bank_note_autenticate_model.keras")
model = tf.keras.models.load_model(model_path)

# Initialize database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)""")
    conn.commit()
    conn.close()

init_db()

# ---------- Routes ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Try another.", "error")
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.", "error")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    prediction_text = None
    if request.method == 'POST':
        try:
            variance = float(request.form['variance'])
            skewness = float(request.form['skewness'])
            curtosis = float(request.form['curtosis'])
            entropy = float(request.form['entropy'])

            input_data = np.array([[variance, skewness, curtosis, entropy]])
            prediction = model.predict(input_data)
            prediction_text = "✅ Authentic Bank Note" if prediction[0][0] > 0.5 else "❌ Fake Bank Note"
        except:
            prediction_text = "Invalid input data."

    return render_template('index.html', username=session['username'], prediction_text=prediction_text)
