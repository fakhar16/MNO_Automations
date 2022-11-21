import git
from flask import Flask, render_template, request
from us_jira import us_jira

app = Flask(__name__)
app.register_blueprint(us_jira)


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


if __name__ == "__main__":
    app.run()
