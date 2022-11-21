import os
import git
from flask import Flask, render_template, request

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
    return os.environ.get('APP_ENV', 'Dev')
    # return render_template("index.html")

# if __name__ == "__main__":
#     print(os.environ.get('APP_ENV', 'Dev'))
#     app.run()
