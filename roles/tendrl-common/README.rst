===============
 Tendrl-common
===============

This role installs `tendrl-common`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-common is installed from sources from github via
``pip``.

The installation is done according to `installation.rst`_ file with the
following exceptions:

- File ``$HOME/.bashrc`` is not edited.
- Python virtualenv is not used, but tendrl python components are installed
  into the system site-packages. Since such operation breaks system
  consistency, it's suggested only for test development, quick test runs on
  latest tendrl code when needed. Actuall testing of a tendrl release should
  be done on packages.


.. _`installation.rst`: https://github.com/Tendrl/common/blob/master/doc/source/installation.rst
.. _`tendrl-common`: https://github.com/Tendrl/common
