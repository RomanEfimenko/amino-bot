import json
import os
import time


def get_justspeackdata():
    """
    Adds a warning to user
    """
    data_file_path = os.getcwd() + '/just_speack_data.json'

    with open(data_file_path, 'r', encoding='UTF-8') as data_file:
        justspeackdata = json.loads(data_file.read())
        data_file.close()

    return justspeackdata

def set_justspeaklasttime(speackdata):
    """
    Adds a warning to user
    """
    data_file_path = os.getcwd() + '/just_speack_data.json'

    if not os.path.exists(data_file_path):
        with open(data_file_path, 'w', encoding='UTF-8') as data_file:
            data_file.write(json.dumps({}))
            data_file.close()

    with open(data_file_path, 'r', encoding='UTF-8') as data_file:
        justspeackdata = json.loads(data_file.read())
        data_file.close()

    justspeackdata[speackdata]['pause_last'] = time.time()

    with open(data_file_path, 'w', encoding='UTF-8') as data_file:
        data_file.write(json.dumps(users_data))
        data_file.close()

    return True

#k = get_justspeackdata()
#print(k["2"]["quests"])
#a = input()
