# import sys, os
# import certifi
# import webbrowser
from Utils.Utils_jira import *
from Utils.Utils_global import *
from flask import Flask, request, render_template, jsonify, Blueprint

# app = Flask(__name__)

us_jira = Blueprint('us_jira', __name__)


@us_jira.route('/us_jira')
def run_us_jira():
    print("Running jira task")
    return render_template("us_jira.html")


@us_jira.route('/get_data_us_jira', methods=['GET', 'POST'])
def get_form_data():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        title = request.form['title']
        assignee = request.form['assignee']
        duedate = request.form['duedate']

        jira = connect_jira(HOST, username, password)

        if jira is None:
            return jsonify({'output': "Invalid Username/Password"})

        if not check_if_user_exist(jira, assignee):
            return jsonify({'output': "Invalid Assignee"})

        return jsonify({'output': "Login successfull"})
    #
    #     ticket_url = read_json_and_create_issues(jira, title, assignee, duedate)
    #     return jsonify({'output': ticket_url})
    #
    # if 'ticket_url' in locals():
    #     return render_template("us_jira.html", ticket_url)

    return render_template("us_jira.html")


def read_json_and_create_issues(jira, title, assignee, duedate):
    global parent_issue
    global JIRA_TICKET_LINK
    parent_issue = None

    data_list = Get_Data_From_Config_File()

    data_list[0]['summary'] = title
    for data in data_list:
        data['assignee']['name'] = assignee
        data['duedate'] = duedate
        issue_key = Create_Issue(jira, data)

        if issue_key is not None:
            JIRA_TICKET_LINK = JIRA_TICKET_LINK + issue_key

    return JIRA_TICKET_LINK

# if __name__=='__main__':
    # path = "C:\\Python\\Python38\\lib\\site-packages\\certifi\\cacert.pem"
    # os.environ['REQUESTS_CA_BUNDLE'] = path
    # open_browser()
    # app.run()