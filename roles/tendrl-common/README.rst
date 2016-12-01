===============
 Tendrl-common
===============

This role installs Tendrl/common. If variable virtualenv_path is specified
than common is installed into virtualenv with provided path. If variable 
install_from is set to "packages" than the component is installed from
packages. If it is set to "source" than it is installed from sources.
Installation is done according to  `tendrl README`_ file except 
few differencies:

- not used virtualenvwrapper
- not edited $HOME/.bashrc

.. _`tendrl README`: https://github.com/Tendrl/common/blob/master/doc/source/installation.rst
