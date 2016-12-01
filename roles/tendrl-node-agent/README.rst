===================
 Tendrl-node-agent
===================
 
This role installs Tendrl/node_agent. If variable virtualenv_path is specified 
than node_agent is installed into virtualenv with provided path. If variable 
install_from is set to "packages" than the component is installed from
packages. If it is set to "source" than it is installed from sources.
Installation is done according to `tendrl README`_ file.

.. _`tendrl README`: https://github.com/Tendrl/node_agent/blob/master/doc/source/installation.rst
