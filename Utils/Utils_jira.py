import os
from jira.client import JIRA


def connect_jira(jira_server, jira_user, jira_password):
    try:
        print("Connecting to JIRA: {}".format(jira_server))
        jira_options = {'server': jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
        return jira
    except Exception as e:
        print("Failed to connect to JIRA: {}".format(e))
        return None


def check_if_user_exist(jira, user_id):
    try:
        jira.user(user_id)
    except:
        return False
    return True


def create_issue(jira, data):
    global parent_issue

    if "parent" not in data:
        if "attachment" not in data:
            parent_issue = jira.create_issue(fields=data)
            return parent_issue.key
        else:
            path = data["attachment"]
            del data["attachment"]

            parent_issue = jira.create_issue(fields=data)
            Add_Attachments(jira, parent_issue, path)
            return parent_issue.key
    else:
        create_subtask(jira, parent_issue, data)
        return None


def create_subtask(jira, parent_issue, data):
    data["parent"]["key"] = parent_issue.key

    if "attachment" not in data:
        jira.create_issue(data)
    else:
        path = data["attachment"]
        del data["attachment"]

        issue = jira.create_issue(fields=data)
        add_attachments(jira, issue, path)


def add_attachments(jira, issue, path):
    files = os.listdir(path)
    for file in files:
        jira.add_attachment(issue=issue, attachment='{}/{}'.format(path, file))