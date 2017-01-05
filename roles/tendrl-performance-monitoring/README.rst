===============================
 Tendrl-performance-monitoring
===============================

This role installs `tendrl-performance-monitoring`_ component.

When variable ``install_from`` is set to ``packages``, the component is
installed from rpm packages via ``yum``. On the other hand when the value is
set to ``source``, tendrl-performance-monitoring is installed from sources
from github via ``npm`` and ``gulp``.

The installation is based on information from `instalaltion documentation`_
with the following exceptions:

* Installed ``fontconfig`` as dependency according to ``gulp`` according to
  `this issue`_.


.. _`tendrl-performance-monitoring`: https://github.com/Tendrl/performance_monitoring
.. _`installation documentation`: https://github.com/Tendrl/performance_monitoring/blob/master/doc/source/installation.rst
.. _`this issue`: https://github.com/Tendrl/tendrl_performance-monitoring/issues/78
