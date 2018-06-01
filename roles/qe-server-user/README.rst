==========================================
 QE Server Role: usmqe user account setup
==========================================

This is a user part of QE Server configuration. The role touches only files in
a home directory of the current ansible user:

* clones usmqe git repositories into homedir
* do ``pip install --user`` of ``usmqe-tests`` requirements
* enables python36 software collection in ``~/.bashrc``

For usage, see ``qe_server*.yml`` playbook files.
