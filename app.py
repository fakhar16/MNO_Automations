from flask import Flask, render_template, request
import git

app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def git_update():
    if request.method == 'POST':
        repo = git.Repo('./MNO_Automations')
        origin = repo.remotes.origin
        repo.create_head('main',
                         origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200

    return 'Wrong event type', 400


@app.route('/')
def home():
    return render_template("index.html")
