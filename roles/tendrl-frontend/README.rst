=================
 Tendrl-frontend
=================

This role installs `tendrl-frontend`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-frontend is installed from sources from github via
``npm`` and ``gulp``.

The installation is based on information from `README file`_ and `Deploying
Tendrl`_ documentation with the following exceptions:

* Installed ``fontconfig`` as dependency according to ``gulp`` according to
  `this issue`_.


.. _`tendrl-frontend`: https://github.com/Tendrl/tendrl_frontend
.. _`README file`: https://github.com/Tendrl/tendrl_frontend/blob/master/README.adoc
.. _`Deploying Tendrl`: https://github.com/Tendrl/documentation/blob/master/deployment.adoc
.. _`this issue`: https://github.com/Tendrl/tendrl_frontend/issues/78
