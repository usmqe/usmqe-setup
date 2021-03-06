===============================================
 Setup of HTTPS for Tendrl UI, API and Grafana
===============================================

This role configures apache to use ssl for Tendrl Web, API and Grafana.

Based on upstream wiki: `Enabling Https on tendrl server
<https://github.com/Tendrl/documentation/wiki/Enabling-Https-on-tendrl-server>`_

See also overview of tendrl ssl related upstream work: `SSL Configuration for
Tendrl
<https://github.com/Tendrl/documentation/wiki/SSL-Configuration-for-Tendrl>`_

Some code was reused from:
https://github.com/Tendrl/tendrl-ansible/pull/46/files

Variables
=========

* ``httpd_ip_address``: public ip address of WA server, where the web is hosted
  (default value provided in the role is valid for standard usmqe environment)
* ``httpd_server_name``: ``ServerName`` of the Tendrl Web
  (default value provided in the role is valid for standard usmqe environment)
* ``httpd_ssl_certificate_key_file``: ``SLCertificateFile`` of the Tendrl Web,
  if not specified, default self signed one is used
* ``httpd_ssl_certificate_file``: ``SSLCertificateKeyFile`` of the Tendrl Web,
  if not specified, default self signed one is used
* ``tendrl_https_redirection``: should we redirect http request to https?
  (default True)
* ``tendrl_https_disable_port_80``: should we disable http port for better
  testing? (default False)
