# app.py
from flask import Flask, session, redirect, url_for, request, render_template, jsonify
import sqlite3
from flask import session
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you have a secret key set


# creating database of users

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()
init_db()

#Database vocabulary

def get_db_connection():
    conn = sqlite3.connect('vocabulary.db')
    conn.row_factory = sqlite3.Row
    return conn

#Login
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('interface'))
        else:
            error_message = '<p style="color: red; text-align: center;">Invalid credentials, you must register first</p>'
            return render_template('index.html', error=error_message)

    return render_template('index.html')

# Registration

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirmation = request.form['confirmation']

        if password != confirmation:
            return 'Passwords do not match'

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('interface'))

    return render_template('register.html')

# User Interface

@app.route('/interface')
def interface():
    username = session.get('username')
    return render_template('interface.html', username = username)

# Saving the word prompted

@app.route('/save_vocab', methods=['POST'])
def save_word():
    word2 = request.form.get('word2')
    translation = request.form.get('translation')
    definition = request.form.get('definition')
    synonyms = request.form.get('synonyms')
    level = request.form.get('level')
    topic = request.form.get('topic')

    if word2 and level:
        conn = get_db_connection()
        existing_word = conn.execute('SELECT * FROM words WHERE word = ?', (word2,)).fetchone()

        if existing_word is None:

            conn.execute('INSERT INTO words (word, translation, definition, synonyms, level, topic) VALUES (?, ?, ?, ?, ?, ?)',
            (word2, translation, definition, synonyms, level, topic))

            conn.commit()
            message = "Added to your dictionary!"
        else:
            message = "You have already added that one!"

        conn.close()
    else:
        message = "No word provided!"

    return render_template('interface.html', message=message)

# Knowing the level of a word

@app.route('/get_level_of_word', methods=['GET', 'POST'])
def get_level_of_word():
    message = None

    if request.method == 'POST' and 'word' in request.form:
        word = request.form.get('word')
        conn = get_db_connection()
        result = conn.execute('SELECT level, translation, definition, synonyms, topic FROM words WHERE word = ?', (word,)).fetchone()
        conn.close()
        if result:
            message = f"""
            <table class="table table-striped table-compact" style="width: 65%; margin: auto;">
                <tr><th style="text-align: center;">Word</th><td>{word}</td></tr>
                <tr><th style="text-align: center;">Level</th><td>{result[0]}</td></tr>
                <tr><th style="text-align: center;">Translation</th><td>{result[1]}</td></tr>
                <tr><th style="text-align: center;">Definition</th><td>{result[2]}</td></tr>
                <tr><th style="text-align: center;">Synonyms</th><td>{result[3]}</td></tr>
                <tr><th style="text-align: center;">Related to the topic</th><td>{result[4]}</td></tr>
            </table>
            """
        else:
            message = f"The word '{word}' does not exist yet. Please add it"

    return render_template('get_level_of_word.html', message=message)

# See the words by level

@app.route('/words_by_level', methods=['GET', 'POST'])
def words_by_level():
    message = None
    words = []
    level = None

    if request.method == 'POST' and 'level' in request.form:
        level = request.form.get('level')
        conn = get_db_connection()
        words = conn.execute('SELECT word, translation, definition, synonyms, topic FROM words WHERE level = ? ORDER BY word ASC', (level,)).fetchall()
        conn.close()
        if not words:
            message = "No elements were found for this level."

    return render_template('words_by_level.html', words=words, level=level, message=message)

# See the words by topic

@app.route('/words_by_topic', methods=['GET', 'POST'])
def words_by_topic():
    topics = []
    words = []
    topic = None

    # Query for topics
    conn = get_db_connection()
    topics = conn.execute("SELECT DISTINCT topic FROM words WHERE topic IS NOT NULL").fetchall()
    conn.close()

    if 'topic' in request.form:
        topic = request.form.get('topic')
        conn = get_db_connection()
        words = conn.execute('SELECT word, translation, definition, synonyms, level FROM words WHERE topic = ? ORDER BY word ASC', (topic,)).fetchall()
        conn.close()

    return render_template('words_by_topic.html', topics=topics, words=words, topic=topic)

# The memo game

@app.route('/memo', methods=['GET', 'POST'])
def memo():
    first_language = None
    second_language = None
    message = None
    words = []
    level = None

    conn = get_db_connection()

    if request.method == 'POST':

        level = request.form.get('level')
        first_language = request.form.get('first_language')
        second_language = request.form.get('second_language')

        if 'level' in request.form:
            words = conn.execute('SELECT word, translation FROM words WHERE level = ?', (level,)).fetchall()
        else:
            words = conn.execute('SELECT word, translation FROM words').fetchall()
    else:
        words = conn.execute('SELECT word, translation FROM words').fetchall()
    conn.close()

    if not words:
        message = "No words found for the selected level."

    return render_template('memo.html', words=words, message = message, first_language = first_language, second_language = second_language)

# Logout

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

#Ensuring all the routes work
if __name__ == '__main__':
    app.run()
