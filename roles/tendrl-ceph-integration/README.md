## Tendrl-ceph-bridge

This role installs Tendrl/ceph_bridge. If variable virtualenv_path is specified than ceph_bridge is installed into virtualenv with provided path. Installation is done according to https://github.com/Tendrl/ceph_bridge/blob/master/doc/source/installation.rst except few differencies:

- editing of /etc/tendrl/tendrl.conf is handled by tendrl-bridge-common role
 
