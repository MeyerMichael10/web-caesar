from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

def load_template(file_name):
    form = "uh oh"
    try:
        file = open("form1.html")
        lines = file.readlines()
        form = "\n".join(lines)
        file.close()
        print(lines)
    except e:
        print(e)
    return form

    

@app.route("/")
def index():
    return load_template("form1.html").format("")
    

@app.route("/", methods = ['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted_text = rotate_string(text, rot)
    
    return load_template("form1.html").format(encrypted_text)



app.run()