===============
 Tendrl-commons
===============

This role installs `tendrl-commons`_ component from packages.

The installation is done according to `installation.rst`_ file with the
following exceptions:

- File ``$HOME/.bashrc`` is not edited.
- Python virtualenv is not used, but tendrl python components are installed
  into the system site-packages. Since such operation breaks system
  consistency, it's suggested only for test development, quick test runs on
  latest tendrl code when needed. Actuall testing of a tendrl release should
  be done on packages.


.. _`installation.rst`: https://github.com/Tendrl/commons/blob/master/doc/source/installation.rst
.. _`tendrl-commons`: https://github.com/Tendrl/commons
