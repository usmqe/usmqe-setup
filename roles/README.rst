===============
 Ansible Roles
===============

This directory contains `Ansible Roles`_.

Roles with ``qe-`` prefix are automating qe tasks (which are not directly based
on Tendrl, Ceph or Gluster documentation), such as particular test setup,
debugging related actions or qe infrastructure deployment.

Roles which installs yum repositories ends with ``-repo`` suffix.

Note that since we reuse ansible roles from official `tendrl-ansible`_, roles
in usmqe-setup should not use the same names. If such conflict happens later
when new role is introduced in tendrl-ansible, we need to rename conflicting
role in usmqe-setup to resolve the name clash.


.. _`Ansible Roles`: https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html
.. _`tendrl-ansible`: https://github.com/Tendrl/tendrl-ansible
