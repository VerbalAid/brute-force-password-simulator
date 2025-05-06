# app.py
from flask import Flask, request, render_template_string
from random import randint

app = Flask(__name__)

# Load index.html as template string for simplicity
with open('index.html') as f:
    INDEX_HTML = f.read()

@app.route('/', methods=['GET'])
def home():
    return render_template_string(INDEX_HTML)

@app.route('/crack', methods=['POST'])
def crack():
    user_password = request.form['password']
    chars = (
      'abcdefghijklmnopqrstuvwxyz'
      'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      '0123456789'
      '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    )
    crack = ""
    attempts = 0
    while crack != user_password:
        crack = ''.join(chars[randint(0, len(chars)-1)]
                        for _ in range(len(user_password)))
        attempts += 1
    return f"<p>Password cracked in {attempts} attempts: <strong>{crack}</strong></p>"

if __name__ == '__main__':
    app.run(debug=False)
