##Tendrl-gluster-bridge

- Requires Ansible 2.1
- Expects CentOS/RHEL 7 hosts

This role installs Tendrl/gluster_bridge. If variable virtualenv_path is specified than gluster_bridge is installed into virtualenv with provided path. Installation is done according to https://github.com/Tendrl/gluster_bridge/blob/master/doc/source/installation.rst except few differencies:

- editing of /etc/tendrl/tendrl.conf is handled by tendrl-bridge-common role
- instead of github.com/Tendrl/gluster_bridge.git is used github.com/shtripat/gluster_bridge.git repo
