============
 Tendrl-api
============

This role installs `tendrl-api`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-api is installed from sources from github via
``pip``.

For installation via packages, it's required to set ``enable_repo`` variable to
``epel``. This ensures that during installation, `epel repository is
available as required`_.

The installation is based on information from `README file`_ and `Deploying
Tendrl`_ documentation with the following exceptions:

* we use *production setup* only by default (see default value of
  ``tendrl_api_exclude_groups`` variable)
* configuration is maintained in ``/etc/tendrl`` for both source and packages
  installation, see details in issue related to `location of tendrl-api
  configuration`_


.. _`tendrl-api`: https://github.com/Tendrl/tendrl-api
.. _`README file`: https://github.com/Tendrl/tendrl-api/blob/master/README.adoc
.. _`Deploying Tendrl`: https://github.com/Tendrl/documentation/blob/master/deployment.adoc
.. _`epel repository is available as required`: https://github.com/Tendrl/tendrl-api/issues/25
.. _`location of tendrl-api configuration`:  https://github.com/Tendrl/tendrl-api/issues/29
