===================================
 Setup ceph-ansible to deploy Ceph
===================================

This role setups Ceph-ansible to be able to install Ceph.
Role can be configured by variables mentioned in ``defaults/main.yml``.
As it is written in ``tasks/main.yml`` ceph-ansible package should be 
preinstalled or available in enabled yum repository.

Example usage of configured ceph-ansible:
# cd to ceph-ansible dir so relative paths can be used
$ cd ``{{ home_dir }}/ceph-ansible from defaults/main.yml``
# /tmp/ansible.cfg is from {{ ansible_conf }} from defaults/main.yml
$ ANSIBLE_CONFIG=/tmp/ansible.cfg ansible-playbook -i ~/ceph_inventory site.yml
