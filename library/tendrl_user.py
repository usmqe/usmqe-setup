#!/usr/bin/python
ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: test_user
short_description: Creates user admin with password admin123 for tendrl.
description:
    - Creates user admin with password admin123 for tendrl
    - There must be installed tendrl-api on the machine where this is ran.
version_added: "1.0"
author: "fbalak@redhat.com"
'''

from ansible.module_utils.basic import AnsibleModule
import re
import requests
import os
import socket
import json

hostname = socket.gethostname()
module = AnsibleModule(argument_spec={})
new_password = "admin123"


def generate_user():
    """Generates admin according to:
    https://github.com/Tendrl/api/blob/master/docs/users.adoc#create-admin-user"""

    os.chdir("/usr/share/tendrl-api")
    return os.popen("RACK_ENV=production rake etcd:load_admin").read()


def parse_password(string):
    """Gets password from user_info. If there is none then it tries to login
    with default password."""

    password = re.compile("\"Password:\s*(?P<pass>[a-zA-Z0-9\._]+)\"")
    admin_exists = re.compile("User named admin already exists.")
    password_found = password.search(string)
    admin_found = admin_exists.search(string)
    if password_found is not None:
        return password_found.group("pass")
    elif admin_found is not None:
        login("admin", new_password)
        response = {"result": "User admin with password {} already exists."
                    .format(new_password)}
        module.exit_json(changed=False, meta=response)


def login(username, password):
    """Login to tendrl server."""

    post_data = {"username": username, "password": password}
    request = requests.post(
        "http://{}/api/1.0/login".format(hostname),
        data=json.dumps(post_data))
    if request.status_code == requests.codes.ok:
        return request.json()
    else:
        response = {"url": request.url, "data": post_data}
        module.fail_json(
            msg="Could not login with these credentials.",
            meta=response)


def change_password(username, password, token):
    """Change password of user and set it's email to username@hostname"""

    post_data = {
        "username": username,
        "password": password,
        "password_confirmation": password,
        "email": "{}@{}".format(username, hostname)}
    request = requests.put(
        "http://{}/api/1.0/users/{}".format(hostname, username),
        data=json.dumps(post_data),
        headers={"Authorization": "Bearer {}".format(token)})
    if request.status_code == requests.codes.ok:
        return request.json()
    else:
        response = {"url": request.url, "data": post_data, "token": token}
        module.fail_json(msg="Request to server failed.", meta=response)


def main():
    username = "admin"
    user_info = str(generate_user())
    password = parse_password(user_info)
    token = login(username, password)["access_token"]
    result = change_password(username, new_password, token)
    response = {"result": result}
    module.exit_json(changed=True, meta=response)


if __name__ == '__main__':
    main()
