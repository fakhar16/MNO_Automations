import os
# import sys
import json

HOST = "https://mobilerndhub.sec.samsung.net/its"
CONFIG_DIRECTORY = 'Config'
JIRA_TICKET_LINK = "https://mobilerndhub.sec.samsung.net/its/browse/"

def Get_Data_From_Config_File():
    data_list = []
    for subdir, dirs, files in os.walk(CONFIG_DIRECTORY):
        for file in files:
            if file.endswith(".json"):
                filename = os.path.join(subdir, file)
                f = open(filename)
                parsed = json.load(f)
                
                if "attachment" in parsed:
                     parsed["attachment"] = "{}/attachments".format(subdir.replace('\\', '/'))
                
                data_list.append(parsed)

    return data_list

# def resource_path(relative_path):
#  """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)   