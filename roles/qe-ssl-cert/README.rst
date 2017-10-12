=================
 SSL Certificate
=================

This role prepare, request and obtain SSL Certificate.

Following variables might be used for changing the default behaviour of this role.

* ``ssl_cert_name``:  Name of the cert and key file (default: "server").
* ``ssl_certs_dir``: Path where to store the certificate (default: "/etc/pki/tls/certs/").
* ``ssl_keys_dir``: Path where to store the private key (default: "/etc/pki/tls/private/").
* ``ssl_owner``: Owner of the cert and private key file (default: "root").
* ``ssl_group``: Group of the cert and private key file (default: "root").
* ``ssl_debug``: Debug mode, do not delete temporary files (default: false).
* ``ssl_cert_perm``: Configure permissions for cert file (default: "0644").
* ``ssl_key_perm``: Configure permissions for key file (default: "0600").
