===================================
 Ansible Group Variables Directory
===================================

This ``group_vars`` directory is a place where it's possible to assign
variables to particular ansible groups, as suggested in `Ansible Best Practices
for Directory Layout`_. See also: `Splitting Out Host and Group Specific
Data`_.

That said, the main reason to have this here is to maintain a list of usmqe
ansible groups, which one can tweak after cloning the repo. No variables are
actually expected to be commited here.

.. _`Ansible Best Practices for Directory Layout`: https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html#directory-layout
.. _`Splitting Out Host and Group Specific Data`: https://docs.ansible.com/ansible/intro_inventory.html#splitting-out-vars
