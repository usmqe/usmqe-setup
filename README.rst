=============
 USMQE Setup 
=============

This repository contains installation and test setup playbooks (along with
other ansible code such as roles) for `usm qe system tests`_ (aka
``usmqe-tests``) of `Tendrl project`_.

Ansible code here is build on top of official upstream ansible playbooks/roles
for Tendrl: `tendrl-ansible`_. If you need to just install Tendrl, just use
`tendrl-ansible`_ instead of this **QE only** repository.


Overview of the repository structure
------------------------------------

We follow `ansible best practices`_ here.

Main top level directories:

* ``group_vars``: `ansible group variables`_ (file for each inventory group)
* ``library``: ansible modules
* ``roles``: ansible roles

All ``*.yml`` files in the root of the repository are `ansible playbooks`_.


Roles
-----

Roles with ``qe-`` prefix are automating qe tasks (which are not directly based
on Tendrl, Ceph or Gluster documentation), such as particular test setup,
debugging related actions or qe infrastructure deployment.

Roles which installs yum repositories ends with ``-repo`` suffix.

Note that since we reuse ansible roles from official `tendrl-ansible`_, roles
in usmqe-setup should not use the same names. If such conflict happens later
when new role is introduced in tendrl-ansible, we need to rename conflicting
role in usmqe-setup to resolve the name clash.

Playbooks
---------

Playbooks starting with ``qe_`` prefix are not meant for direct Tendrl
deployment, but for other tasks which QE team needed to automate, eg.:

* ``qe_server.yml`` playbook automates deployment of QE Server machine, where
  `usm qe system tests`_ are installed and executed/managed from
* ``qe_evidence*.yml`` playbooks automate log/evidence gathering process


Requirements
------------

You need to install ansible 2.x (`ansible from current Fedora or EPEL`_).

We also assume that storage or tendrl servers (machines you configure with
playbooks stored in this repository) run CentOS 7 distribution.

.. TODO: update this statement when we include support for other distros (which
.. is the current plan)

Since playbooks there reuses ansible roles from `tendrl-ansible`_, you need to
make those roles available, which means downloading (or cloning) tendrl-ansible
and pointing ``ANSIBLE_ROLES_PATH`` variable to roles directory of
tendrl-ansible like this::

    ANSIBLE_ROLES_PATH=/home/usmqe/tendrl-ansible/roles ansible-playbook -i ci_usm1.hosts ci_default.yml


Code style of YAML files
------------------------

We use `yamllint`_ tool to check syntax and formatting of yaml files in
this repository. The rules we enforce (stored in ``.yamllint`` file) are based
on `yamllint configuration of ansible project`_.

To run the checks, install ``yamllint`` (use either `Fedora/CentOS yamllint
packages`_ or PyPI via ``pip``) and run::

    $ yamllint .

This check is also run by `usmqe-setup Travis CI job`_ for each pull request.


Documentation
-------------

To find more details or to get a whole picture how this repository relates to
system tests, see `usm qe documentation`_.


License
-------

Distributed under the terms of the `Apache License 2.0`_ license.


.. _`Tendrl project`: http://tendrl.org/
.. _`usm qe system tests`: https://github.com/usmqe/usmqe-tests/
.. _`usm qe documentation`: https://usmqe-tests.readthedocs.io/en/latest/
.. _`ansible best practices`: https://docs.ansible.com/ansible/playbooks_best_practices.html
.. _`ansible group variables`: https://docs.ansible.com/ansible/intro_inventory.html#splitting-out-vars
.. _`ansible playbooks`: https://docs.ansible.com/ansible/playbooks_intro.html
.. _`Apache License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`ansible from current Fedora or EPEL`: https://apps.fedoraproject.org/packages/ansible
.. _`yamllint`: https://yamllint.readthedocs.io/en/latest/
.. _`yamllint configuration of ansible project`: https://github.com/ansible/ansible/blob/devel/.yamllint
.. _`Fedora/CentOS yamllint packages`: https://apps.fedoraproject.org/packages/yamllint
.. _`usmqe-setup Travis CI job`: https://travis-ci.org/usmqe/usmqe-setup
.. _`tendrl-ansible`: https://github.com/Tendrl/tendrl-ansible
