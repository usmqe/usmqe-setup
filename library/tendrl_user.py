#!/usr/bin/python
'''
module: test_user
short_description: Changes 'usm_username' user password to _password_from_module_argument_
via Tendrl API.
description:
    - Module reads from confile(module argument 'conf_path') 'usm_username',
      'usm_password' and 'usm_api_url'.
    - There must be installed tendrl-api on the machine where this is ran.
    - Usage: ansible -i _inventory_ -m tendrl_user -a "conf_path='_usm.ini.path_'" localhost
version_added: "1.0"
author: "fbalak@redhat.com", "mkudlej@redhat.com"
'''

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: test_user
short_description: Changes 'usm_username' user password to _password_from_module_argument_
via Tendrl API.
description:
    - Module reads from confile(module argument 'conf_path') 'usm_username', 
      'usm_password' and 'usm_api_url'.
    - There must be installed tendrl-api on the machine where this is ran.
version_added: "1.0"
    - Usage: ansible -i _inventory_ -m tendrl_user -a "conf_path='_usm.ini.path_'" localhost
author: "fbalak@redhat.com", "mkudlej@redhat.com"
'''

import json
import ConfigParser
import requests
from ansible.module_utils.basic import AnsibleModule

MODULE = AnsibleModule(
    argument_spec=dict(
        conf_path=dict(required=True, type='str'),
        new_password=dict(required=True, type='str')
        )
    )

def login(api_url, username, password):
    """Login to tendrl server."""

    post_data = {"username": username, "password": password}
    request = requests.post(
        "{}login".format(api_url),
        data=json.dumps(post_data))
    if request.status_code == requests.codes["ok"]:
        return request.json()
    else:
        response = {"url": request.url, "data": post_data}
        MODULE.fail_json(
            msg="Could not login with these credentials.",
            meta=response)

def change_password(api_url, username, password, token):
    """Change password of user and set it's email to username@hostname"""

    post_data = {
        "username": username,
        "password": password,
        "password_confirmation": password,
        "email": "{}@{}".format(username, 'localhost.localdomain')}
    request = requests.put(
        "{}users/{}".format(api_url, username),
        data=json.dumps(post_data),
        headers={"Authorization": "Bearer {}".format(token)})
    if request.status_code == requests.codes["ok"]:
        return request.json()
    else:
        response = {"url": request.url, "data": post_data, "token": token, "text": request.text}
        MODULE.fail_json(msg="Request to server failed.", meta=response)


def main():
    """Main function"""

    conf_path = MODULE.params['conf_path']
    new_password = MODULE.params['new_password']
    config = ConfigParser.SafeConfigParser()
    config.read(conf_path)

    username = config.get('usmqepytest', 'usm_username')
    password = config.get('usmqepytest', 'usm_password')
    api_url = config.get('usmqepytest', 'usm_api_url')

    token = login(api_url, username, password)["access_token"]
    if password == new_password:
        MODULE.exit_json(changed=False)

    result = change_password(api_url, username, new_password, token)
    response = {"result": result}

    config.set('usmqepytest', 'usm_password', new_password)
    with open(conf_path, 'wb') as conffile:
        config.write(conffile)

    MODULE.exit_json(changed=True, meta=response)

if __name__ == '__main__':
    main()
