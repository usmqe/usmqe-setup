=========================
 Tendrl-ceph-integration
=========================

This role installs Tendrl/ceph_integration. If variable virtualenv_path is 
specified than ceph_integration is installed into virtualenv with provided 
path. If variable use_source is set to true than the component is installed 
from sources. Otherwise it is installed from packages. Installation is done 
according to `tendrl README`_ file except few differencies:

- editing of /etc/tendrl/tendrl.conf is handled by tendrl-node-agent role
 
.. _`tendrl README`: https://github.com/Tendrl/ceph_integration/blob/master/doc/source/installation.rst
