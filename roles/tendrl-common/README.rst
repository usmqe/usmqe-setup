===============
 Tendrl-common
===============

This role installs `tendrl-common`_.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-common is installed from sources into python
virtualenv.

The installation is done according to `installation.rst`_ file with the
following exceptions:

- ``$HOME/.bashrc`` file is not edited
- location of python virtualenv is different, see default for
  ``virtualenv_path`` variable


.. _`installation.rst`: https://github.com/Tendrl/common/blob/master/doc/source/installation.rst
.. _`tendrl-common`: https://github.com/Tendrl/common
