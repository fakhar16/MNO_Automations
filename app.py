from flask import Flask, render_template, request
import git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/fakhar16/MNO_Automations')
        origin = repo.remotes.origin
        # repo.create_head('master',
        #                  origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")