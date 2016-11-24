============
 Tendrl-frontend
============

This role installs tendrl frontend component, aka Tendrl/frontend. Role was created
according to `tendrl deployment.adoc`_ file.

To use the role in the current state, you need to redefine repo related
variables in this way::

    tendrl_frontend_repo_url: git://github.com/Tendrl/tendrl_frontend.git
    tendrl_frontend_repo_branch: master

.. _`tendrl deployment.adoc`: https://github.com/Tendrl/tendrl_frontend/blob/master/docs/deployment.adoc
