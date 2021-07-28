import os, json
from flask import Flask, render_template
app = Flask(__name__)


def get_flowers(path):
    flowers = []
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        lst
        for name in lst:
            flowers.append(name)
            
    return flowers

@app.route('/')
def hello_world():
    files = get_flowers('static/images')
    return render_template('index.html', files=files)
    #return json.dumps(files)
