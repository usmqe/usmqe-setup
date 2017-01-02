===================
 Tendrl-node-agent
===================
 
This role installs `tendrl-node-agent`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-node-agent is installed from sources from github via
``pip``.

The installation is based on information from:

* `installation.rst`_
* `README file`_

with the following exceptions:

* installation from sources is not done via Python virtualenv
* ceph or gluster integration components are not installed in this role
* we don't install, configure or explicitly depend on etcd

Open issues:

* https://github.com/Tendrl/node_agent/issues/87
* https://github.com/Tendrl/node_agent/issues/88
* https://github.com/Tendrl/node_agent/issues/89

.. _`installation.rst`: https://github.com/Tendrl/node_agent/blob/master/doc/source/installation.rst
.. _`README file`: https://github.com/Tendrl/node_agent/blob/master/README.rst
.. _`tendrl-node-agent`: https://github.com/Tendrl/node_agent
