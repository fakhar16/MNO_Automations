from flask import Flask, render_template
import git

app = Flask(__name__ )

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.repo('./MNO_Automations')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")