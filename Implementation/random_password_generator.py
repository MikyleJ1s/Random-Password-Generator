from flask import Flask, redirect, render_template, request, url_for
import random, string
import numpy as np


app = Flask(__name__)

@app.route('/')
def home_page():
    return redirect(url_for('generate_password'))

@app.route('/generate_password', methods=['GET', 'POST'])
def generate_password():

    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase

    digits = string.digits

    punctuation = string.punctuation
    
    if request.method == 'POST':
        use_lowercase = request.form.get("use_lowercase")
        use_uppercase = request.form.get("use_uppercase")
        use_digits = request.form.get("use_digits")
        use_punctuation = request.form.get("use_punctuation")
        password_range = []
        
        if request.form['use_length']!="":
            if not use_lowercase and not use_uppercase and not use_digits and not use_punctuation:
                # password_range = ascii_lowercase + ascii_uppercase + digits + punctuation
                return render_template('home_page.html', unique_password = "")
        
            else:
                if use_lowercase:
                    password_range += ascii_lowercase
                if use_uppercase:
                    password_range += ascii_uppercase
                if use_digits:
                    password_range += digits
                if use_punctuation:
                    password_range += punctuation        
    
            return render_template('home_page.html', unique_password = "".join(random.choices(password_range, k=int(request.form['use_length']))))
        return render_template('home_page.html', unique_password = "")
    
    elif request.method == 'GET':
        return render_template('home_page.html')

if __name__ == '__main__':
    app.run(debug=True)