============
 Tendrl-api
============

This role installs tendrl api component, aka Tendrl/tendrl. Role was created
according to `tendrl README`_ file. The last step involving starting server is
not present.

Since the configuration of etcd for tendrl is not properly documented, this
role is not complete.

To use the role in the current state, you need to redefine repo related
variables in this way::

    tendrl_api_repo_url: git://github.com/anivargi/tendrl.git
    tendrl_api_repo_branch: gluster-create-volume-api

.. _`tendrl README`: https://github.com/anivargi/tendrl/blob/gluster-create-volume-api/README.md
