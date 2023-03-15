# modules used ...
from flask import Flask, redirect, render_template, request, url_for, Response
import random, string, logging, time

# logger configurations ...
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs.log", filemode='a', level = logging.DEBUG, format = f"%(asctime)s %(levelname)s %(message)s")

def password_generator(password_range, length):
    return "".join(random.choices(password_range, k=int(length)))

app = Flask(__name__)

# main page logic ...
@app.route('/', methods=['GET', 'POST'])
def generate_password():
    # letters available ....
    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    # digts available ...
    digits = string.digits
    # punctuation available ...
    punctuation = string.punctuation
    
    if request.method == 'POST':
        
        # check the user input ...
        
        app.logger.info("Checking the user input")
        
        use_lowercase = request.form.get("use_lowercase")
        use_uppercase = request.form.get("use_uppercase")
        use_digits = request.form.get("use_digits")
        use_punctuation = request.form.get("use_punctuation")
                
        password_range = []
        
        # check if a length was specified ...
        if request.form['use_length']!="":
            # length was given now check if any of the customization boxes was checked ...
            if not use_lowercase and not use_uppercase and not use_digits and not use_punctuation:
                # no box has been checked so return an error message ... 
                app.logger.info("Can't return a password because no customization was provided")
                return Response(status=204) 
                #return render_template('home_page.html', unique_password = "") # this refreshes the whole page ...

            # length was given and at least one of the boxes was ticked ...
            else:
                # check which boxes were chosen ...
                if use_lowercase:
                    password_range += ascii_lowercase
                if use_uppercase:
                    password_range += ascii_uppercase
                if use_digits:
                    password_range += digits
                if use_punctuation:
                    password_range += punctuation   
            
            # output a password according to the lenght and customization given ...
            app.logger.info("Returning a unique password")
            return render_template('home_page.html', unique_password = password_generator(password_range, request.form['use_length']))
        
        # length was not given so return an error ...
        app.logger.info("Can't return a password because no length was provided")
        return Response(status=204) 
        #return render_template('home_page.html', unique_password = "") # this refreshes the whole page ...
    
    elif request.method == 'GET':
        app.logger.info("Going to the main page")
        return render_template('home_page.html')

if __name__ == '__main__':
    app.run(debug=True)