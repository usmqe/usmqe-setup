===================================
 Setup ceph-ansible to deploy Ceph
===================================

This role installs ceph-ansible package and setup it to be able to install Ceph.
Role can be configured by variables mentioned in ``defaults/main.yml``.
As it is written in ``tasks/main.yml`` ceph-ansible package should be 
preinstalled or available in enabled yum repository.
