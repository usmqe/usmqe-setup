=============
 USMQE Setup 
=============

This repository contains installation and test setup playbooks (along with
other ansible code such as roles) for `usm qe integration tests`_ (aka
``usmqe-tests``) of `Tendrl project`_.

Overview of the repository structure
------------------------------------

We follow `ansible best practices`_ here.

Main top level directories:

* ``roles``: ansible roles
* ``group_vars``: `ansible group variables`_ (file for each inventory group)

License
-------

Distributed under the terms of the `Apache License 2.0`_ license.


.. _`Tendrl project`: https://github.com/Tendrl/
.. _`usm qe integration tests`: https://github.com/Tendrl/usmqe-tests/
.. _`ansible best practices`: https://docs.ansible.com/ansible/playbooks_best_practices.html
.. _`ansible group variables`: https://docs.ansible.com/ansible/intro_inventory.html#splitting-out-vars
.. _`Apache License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
