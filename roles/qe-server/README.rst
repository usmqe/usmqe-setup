================
 QE Server Role
================

This role configures the machine for execution of usmqe integration tests.

Sudoers configuration
=====================

This role configures sudo to allow ``usmqe`` unix group (which is created along
with user account of the same name in this role) to do anything as root, see
``20_usmqe_sudoers`` file.

Here is an example of ansible playbook which runs locally and switches to root
user account via sudo::

     - name: Do something as root on usmqe server locally
       hosts: localhost
       connection: local
       become: yes
       become_user: root
       become_method: sudo

       ...


Xvfb Service
============

This role also installs systemd unit file  for `Xvfb server`_ named
``Xvfb.service`` to simplify management of Xvfb server process.

The service uses display ``:0``, which is hardcoded in the service ini file.

So for example to start Xvfb server, do::

    # systemctl start Xvfb

Also note that the service name can be used with with journald as well::

	# journalctl -u Xvfb
	-- Logs begin at Thu 2016-12-01 05:18:45 EST, end at Fri 2017-01-13 11:40:06 EST. --
	Jan 13 11:40:06 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Started Xvfb virtual framebuffer X server for X Version 11.
	Jan 13 11:40:06 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Starting Xvfb virtual framebuffer X server for X Version 11...

Acknowledgement:

* https://gist.github.com/ypandit/f4fe751bcbf3ee6a32ca
* http://superuser.com/a/912648/295282

.. _`Xvfb server`: https://en.wikipedia.org/wiki/Xvfb
.. _`systemd template unit file`: https://fedoramagazine.org/systemd-template-unit-files/


x11vnc Service
==============

Another systemd service installed in this role is ``x11vnc.service``.

Note that the service (following details are hardcoded in service ini file):

* uses display ``:0``
* listens on tcp port ``5900`` (and another task in qe-server role opens this
  port in firewalld)

Example of usage: under root user account, start vnc server::

    # systemctl start x11vnc

Note that if ``Xvfb`` service is not running, systemd will try to start it
before starting ``x11vnc``.

Then under ``usmqe`` user account, one can just use the diplay::

    $ export DISPLAY=:0
    $ firefox

To connect to remove X server running on usmqe server machine from local
workstataion, run::

    $ vncviewer qeserver.usmqe.example.com:5900


Examples
========

Inspecting status of the vnc server::

    # systemctl status x11vnc
    ● x11vnc.service - x11vnc provides VNC connections to real X11 displays
       Loaded: loaded (/etc/systemd/system/x11vnc.service; enabled; vendor preset: disabled)
       Active: active (running) since Mon 2017-01-16 08:32:01 EST; 25s ago
      Process: 28565 ExecStart=/usr/bin/x11vnc -display :0 -bg -nopw -xkb -forever -shared -logfile /var/log/x11vnc.0.log (code=exited, status=0/SUCCESS)
     Main PID: 28566 (x11vnc)
       CGroup: /system.slice/x11vnc.service
               └─28566 /usr/bin/x11vnc -display :0 -bg -nopw -xkb -forever -shared -logfile /var/log/x11vnc.0.log

    Jan 16 08:32:01 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Starting x11vnc provides VNC connections to real X11 displays...
    Jan 16 08:32:01 dhcp-126-60.lab.eng.brq.redhat.com x11vnc[28565]: PORT=5900
    Jan 16 08:32:01 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Started x11vnc provides VNC connections to real X11 displays.
