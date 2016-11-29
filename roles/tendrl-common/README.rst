===============
 Tendrl-common
===============

This role installs Tendrl/common. If variable virtualenv_path is specified
than common is installed into virtualenv with provided path. If variable 
use_source is set to true than the component is installed from sources. 
Otherwise it is installed from packages. Installation is done according 
to  `tendrl README`_ file except few differencies:

- not used virtualenvwrapper
- not eddited $HOME/.bashrc

.. _`tendrl README`: https://github.com/Tendrl/common/blob/master/doc/source/installation.rst
