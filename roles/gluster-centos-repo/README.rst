===================
Gluster-centos-repo
===================

This role adds Gluster repo maintained by `CentOS Storage SIG`_. Note that
packages installed by this role are not signed.

The role is configured by variable ``gluster_centos_repo`` which could be
eiter:

* ``nightly``: Latest nightly builds from ``artifacts.ci.centos.org``.
  When used, ``epel`` role is added into dependencies of this role so that
  EPEL_ is installed and enabled as well (see explnanation below).
* ``3-12``: GlusterFS version 3.12
* ``3-11``: GlusterFS version 3.11
* ``3-10``: GlusterFS version 3.10
* ``3-9``: GlusterFS version 3.9

Also note:

* Nightly builds repo is the default.
* You can't specify repo url directly, you need to select one release from the
  list shown above.
* It could happen that for nightly or rc builds, you would need to enable EPEL_
  via ``epel`` role (eg. when you see error like ``Error: Package ...
  Requires: liburcu-cds.so.6()(64bit)``, it means you are missing
  `userspace-rcu`_).

.. _`CentOS Storage SIG`: https://wiki.centos.org/SpecialInterestGroup/Storage
.. _EPEL: https://fedoraproject.org/wiki/EPEL
.. _`userspace-rcu`: https://apps.fedoraproject.org/packages/userspace-rcu
