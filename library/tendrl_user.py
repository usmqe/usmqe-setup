 
#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
import subprocess
import re

def generate_user():
    return subprocess.Popen("RACK_ENV=production rake etcd:load_admin",
        cwd="/usr/share/tendrl-api",
        stdout=subprocess.PIPE)

def parse_password(string):
    pattern = re.compile("\"Password:\s*(?P<pass>[a-zA-Z0-9\._]+)\"")
    match = pattern.search(string)
    if match is not None:
        return match.group("pass")

def login(username, password):
    request = requests.post(
        "{{ inventory_hostname }}/api/1.0/login",
        {"username": username, "password": password})
    return request.json()

def change_password(username, password, token):
    request = requests.post(
        "{{ inventory_hostname }}/api/1.0/user/{}".format(username),
        {"username": username, "password": password},
        headers={"Authorization": "Bearer {}".format(token)})
    return request.json()

def main():

    username = "admin"
    module = AnsibleModule(argument_spec={})
    user_info = generate_user()
    password = parse_password(user_info)
    token = login(username, password)["access_token"]
    result = change_password(username, "admin", token)
    response = {"result": result}
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':  
    main()
