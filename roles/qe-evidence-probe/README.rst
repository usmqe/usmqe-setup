=======================
 qe-evidence-probe role
=======================

This ansible role automates and standardizes the way QE team collects
additional evidence from test machines.

Description
-----------

This role creates special temporary directory ``/etc/usmqe/`` on a remote
machine and stores there output of few predefined commands (such as ``rpm
-qa``, ``yum repolist``, ``lsblk``, ``sestatus``, ...). This way, our team can
store a full list of useful information for debugging and analysis.
