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

All ``*.yml`` files in the root of the repository are `ansible playbooks`_.


Playbooks
---------

Playbooks starting with ``qe_`` prefix are not meant for direct Tendrl
deployment, but for other tasks which QE team needed to automate, eg.:

* ``qe_server.yml`` playbook automates deployment of QE Server machine, where
  `usm qe integration tests`_ are installed and executed/managed from
* ``qe_evidence*.yml`` playbooks automate log/evidence gathering process

Note that playbooks with ``skyrings`` in it's name are not supposed to be used
for Tendrl setup either. These files are there for a reference how particular
deployment/setup task should be done, eg:

* ``firewall.skyrings.yml`` firewall setup for skyrings project
* ``services.skyrings.yml`` service management for skyrings project

To see more details, check readme files of ansible roles used in the playbook.


Requirements
------------

You need to install ansible 2.x (`ansible from current Fedora or EPEL`_).

We also assume that storage or tendrl servers (machines you configure with
playbooks stored in this repository) run CentOS 7 distribution.

.. TODO: update this statement when we include support for other distros (which
.. is the current plan)


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
integartion tests, see `usm qe documentation`_.


License
-------

Distributed under the terms of the `Apache License 2.0`_ license.


.. _`Tendrl project`: http://tendrl.org/
.. _`usm qe integration tests`: https://github.com/Tendrl/usmqe-tests/
.. _`usm qe documentation`: https://usmqe-tests.readthedocs.io/en/latest/
.. _`ansible best practices`: https://docs.ansible.com/ansible/playbooks_best_practices.html
.. _`ansible group variables`: https://docs.ansible.com/ansible/intro_inventory.html#splitting-out-vars
.. _`ansible playbooks`: https://docs.ansible.com/ansible/playbooks_intro.html
.. _`Apache License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`ansible from current Fedora or EPEL`: https://apps.fedoraproject.org/packages/ansible
.. _`yamllint`: https://yamllint.readthedocs.io/en/latest/
.. _`yamllint configuration of ansible project`: https://github.com/ansible/ansible/blob/devel/.yamllint
.. _`Fedora/CentOS yamllint packages`: https://apps.fedoraproject.org/packages/yamllint
.. _`usmqe-setup Travis CI job`: https://travis-ci.org/Tendrl/usmqe-setup
