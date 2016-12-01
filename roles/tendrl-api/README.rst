============
 Tendrl-api
============

This role installs tendrl api component, aka Tendrl/tendrl. Role was created
according to `tendrl README`_ file. If variable install_from is set to 
"packages" than the component is installed frompackages. If it is 
set to "source" than it is installed from sources. The last step 
involving starting server is not present.

For installation via packages is currently needed to have variable use_epel 
set to true. This variable ensures that during installation is enabled epel 
repository.

.. _`tendrl README`: https://github.com/anivargi/tendrl/blob/gluster-create-volume-api/README.md
