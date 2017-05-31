================
 QE-Tendrl-repo
================

This role enables required Tendrl repositories and installs their
public gpg rpm keys (if configured).

By default `tendrl/release copr`_ and `tendrl/dependencies copr`_ repositories.

The default repositories might be overwritten by following variables:
  - tendrl_repo_url
  - tendrl_repo_gpgkey_url
  - tendrl_dependencies_repo_url
  - tendrl_dependencies_repo_gpgkey_url

If gpgkey url set to empty string (""), gpgcheck is disabled.

.. _`tendrl/release copr`: https://copr.fedorainfracloud.org/coprs/tendrl/release/
.. _`tendrl/dependencies copr`: https://copr.fedorainfracloud.org/coprs/tendrl/dependencies/
