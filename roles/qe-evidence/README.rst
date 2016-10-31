==================
 qe-evidence role
==================

This ansible role automates and standarzides the way QE team collects log
files and other evidence from test machines.

Description
-----------

The role basically downloads all directories specified in ``evidence_dirs``
variable and all files in ``evidence_files`` - you can either use defaults
or redefine them in a playbook in which you use the role.

To specify a local directory where all the remote files (logs and such) will
be downloaded, you need to specify ``evidence_target`` variable. In this
directory, a new subdirectory for each machine is created and the under each
such host directory, files follows standard hierarchy. So for example,
when you add ``/etc/resolv.conf`` file into ``evidence_files``, ansible will
download it from each machine (as you specify in the playbook) into local
file ``${evidence_targe}/${machine_hostname}/etc/resolv.conf``.

Usage
-----

Here is the minimal example how to use the role::


    $ ansible-playbook -i mbukatov-usm3.hosts --extra-vars='evidence_target=/home/martin/tmp/bz-123/' qe_evidence.yml

Note that in this simple example, we:

* use minimal ``qe_evidence`` playbook
* don't redefine ``evidence_{dirs,files}`` variables and use role defautls
* still need to specify ``evidence_target`` variable

Full example
------------

So let's see a full example with some additional description. First we create
local evidence directory, where we are going to store the evidence files (log,
config or other files from remote machines)::

    $ mkdir -p ~/tmp/bz-1343651

Since we don't need to download any particular files in this example,
we can just use the default playbook without changing either ``evidence_dirs``
or ``evidence_files`` variable::

	$ cat qe_evidence.yml
	---

	# Minimal playbook for qe-evidence role (role defaults are used)

	- name: Download all logs and all configuration from all machines
	  hosts: all
	  user: root
	  roles:
		- qe-evidence

Then to run the playbook, we need to specify the ``evidence_target`` variable::

    $ ansible-playbook -i mbukatov-usm3.hosts --extra-vars='evidence_target=/home/martin/tmp/bz-1343651/' qe_evidence.yml

When ansible finishes, we will find the evidence files in the evidence target
directory::

    $ cd /home/martin/tmp/bz-1343651/
    $ ls
    mbukatov-usm3-mon1.example.tendrl.org
    mbukatov-usm3-mon2.example.tendrl.org
    mbukatov-usm3-mon3.example.tendrl.org
    mbukatov-usm3-node1.example.tendrl.org
    mbukatov-usm3-node2.example.tendrl.org
    mbukatov-usm3-node3.example.tendrl.org
    mbukatov-usm3-node4.example.tendrl.org
    mbukatov-usm3-server.example.tendrl.org
    $ ls -l mbukatov-usm3-server.example.tendrl.org/
    total 16
    drwxr-xr-x. 102 martin martin 12288 Jul 25 15:44 etc
    drwxrwxr-x.   3 martin martin  4096 Aug  1 15:54 var

The nice thing about this approach is that when you need to download particular
directories or files from all machines, you start with the standart playbook
and redefine ``evidence_files`` and/or ``evidence_dirs`` variables and just run
ansible. You don't need to figure out the rsync options yourself and the
result will follow some standard structure.
