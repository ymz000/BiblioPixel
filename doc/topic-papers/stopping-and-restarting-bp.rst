How to stop or restart ``bp``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While some Animations can have a specific, fixed length like ten seconds, most
of them go on indefinitely.  Sometimes you want to tell ``bp`` to stop running,
or you want to tell it to restart from the beginning again.


1. Control-C
~~~~~~~~~~~~~~~~~~~~~

The simplest way to stop ``bp`` is using Control-C - hold down the Control or
CTR key and press C.

Control-C interrupts almost any command line program, not just ``BiblioPixel``.
It must be done in the command line or terminal which is running ``bp``.


2. Unix signals
~~~~~~~~~~~~~~~~~~~~~

This is an advanced section which can safely be skipped on first reading!

A more versatile way (which unfortunately does not work on Windows) is to send a
`Unix signal <https://www.tutorialspoint.com/unix/unix-signals-traps.htm>`_
to the ``bp`` process.

``bp`` understands three Unix signals:

``SIGINT``
  Shut ``bp`` down in a controlled fashion, turning off all lights:
  equivalent to typing Control-C.

``SIGTERM``
  Shut ``bp`` down immediately.

``SIGHUP``
  Stop the running ``bp`` Project in a controlled fashion, create a new
  Project by re-reading the originalo Project file, then run it.

``SIGHUP`` is particularly useful for developers who want to restart their
application with a new Animation without taking the several seconds it would
take to bring ``bp`` down and back up again.

A tiny bash utility ``bp-pid`` is installed with BiblioPixel to report on the
process ID that's running ``bp``.

For example, to send a ``SIGHUP`` to the running ``bp`` process, if any, use
this command line:

.. code-block:: bash

    $ kill -hup `bp-pid`

This will restart ``bp`` if it is running, otherwise cause an error.

.. bp-code-block:: footer

   shape: [64, 13]
   animation: $bpa.strip.LarsonScanners.LarsonRainbow
