================
 QE Server Role
================

This role configures the machine for execution of usmqe integration tests.

Xvfb Service
============

This role also installs `systemd template unit file`_  for `Xvfb server`_ named
``Xvfb@.service`` to simplify management of Xvfb server process(es).

Template unit file was used to be able to run multiple Xvfb servers for
different X server displays.

So for example to start Xvfb server for display ``:0``, use service named
``Xvfb@:0`` like this::

    # systemctl start Xvfb@:0

While you can start another one on display ``:1`` at the same time::

    # systemctl start Xvfb@:1

The full service name can be used with any other systemctl operation, eg. to
inspect the status just run::

    # systemctl status Xvfb@:0
    ● Xvfb@:0.service - Xvfb virtual framebuffer X server for X Version 11
       Loaded: loaded (/etc/systemd/system/Xvfb@.service; disabled; vendor preset: disabled)
       Active: active (running) since Fri 2017-01-13 11:40:06 EST; 30s ago
     Main PID: 16385 (Xvfb)
       CGroup: /system.slice/system-Xvfb.slice/Xvfb@:0.service
               └─16385 /usr/bin/Xvfb :0 -screen 0 1280x1024x16 -noreset

    Jan 13 11:40:06 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Started Xvfb virtual framebuffer X server for X Version 11.
    Jan 13 11:40:06 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Starting Xvfb virtual framebuffer X server for X Version 11...

Or with journald::

	# journalctl -u Xvfb@:0
	-- Logs begin at Thu 2016-12-01 05:18:45 EST, end at Fri 2017-01-13 11:40:06 EST. --
	Jan 13 11:40:06 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Started Xvfb virtual framebuffer X server for X Version 11.
	Jan 13 11:40:06 dhcp-126-60.lab.eng.brq.redhat.com systemd[1]: Starting Xvfb virtual framebuffer X server for X Version 11...

Acknowledgement:

* https://gist.github.com/ypandit/f4fe751bcbf3ee6a32ca
* http://superuser.com/a/912648/295282

.. _`Xvfb server`: https://en.wikipedia.org/wiki/Xvfb
.. _`systemd template unit file`: https://fedoramagazine.org/systemd-template-unit-files/
