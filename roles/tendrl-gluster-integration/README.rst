============================
 Tendrl-gluster-integration
============================

This role installs `tendrl-gluster-integration`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-gluster-integration is installed from sources from
github via ``pip``.

The installation is based on information from `installation.rst`_ with the
following exceptions:
 
- we don't install `tendrl-common` component once again in this role (this
  is handled either by rpm dependencies for ``install_from == packages`` or
  via ansible metadata dependencies when ``install_from == source``)
- we don't install `/etc/tendrl/tendrl.conf` configuration file, which is owned
  by `tendrl-node-agent` component

Open issues:

* https://github.com/Tendrl/gluster_integration/issues/86
* https://github.com/Tendrl/gluster_integration/issues/87
* https://github.com/Tendrl/node_agent/issues/99

 
.. _`tendrl-gluster-integration`: https://github.com/Tendrl/gluster_integration
.. _`installation.rst`: https://github.com/Tendrl/gluster_integration/blob/master/doc/source/installation.rst
