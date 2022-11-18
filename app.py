import webbrowser
from flask import *

app = Flask(__name__ )

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__=='__main__':
    open_browser()
    app.run(port=5000)