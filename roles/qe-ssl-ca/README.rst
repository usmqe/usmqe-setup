=================
 QE SSL CA Setup
=================

This role downloads OpenSSL Certificate Authority file of QE team and imports
it into system so that it's trusted on the machine by default.

The role is expected to be used on qe-server and client machine only.

Mandatory ansible variables:

* ``ca_usmqe_cert_url`` is url of QE CA cert file
