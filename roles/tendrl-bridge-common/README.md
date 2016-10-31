##Tendrl-bridge-common

- Requires Ansible 2.1
- Expects CentOS/RHEL 7 hosts

This role installs Tendrl/bridge_common. If variable virtualenv_path is specified than bridge_common is installed into virtualenv with provided path. Installation is done according to https://github.com/Tendrl/bridge_common/blob/master/doc/source/installation.rst except few differencies:

- not used virtualenvwrapper
- not eddited $HOME/.bashrc
