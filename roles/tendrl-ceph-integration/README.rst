=========================
 Tendrl-ceph-integration
=========================

This role installs `tendrl-ceph-integration`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-ceph-integration is installed from sources from
github via ``pip``.

The installation is based on information from `installation.rst`_ with the
following exceptions:

- we don't install `tendrl-common` component once again in this role (this
  is handled either by rpm dependencies for ``install_from == packages`` or
  via ansible metadata dependencies when ``install_from == source``)
- we don't install `/etc/tendrl/tendrl.conf` configuration file, which is owned
  by `tendrl-node-agent` component

Open issues:

* https://github.com/Tendrl/node_agent/issues/99
* https://github.com/Tendrl/ceph_integration/issues/57


.. _`tendrl-ceph-integration`: https://github.com/Tendrl/ceph_integration
.. _`installation.rst`: https://github.com/Tendrl/ceph_integration/blob/master/doc/source/installation.rst
