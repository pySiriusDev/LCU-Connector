:orphan:

:py:mod:`lcu_connector.riot`
============================

.. py:module:: lcu_connector.riot


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   lcu_connector.riot.Lockfile
   lcu_connector.riot.LeaguClient




.. py:class:: Lockfile(path)

   Class that manages the lockfile and its data.

   .. attribute:: path

      The path of the lockfile.

      :type: str

   .. attribute:: name

      The name of the lockfile.

      :type: str

   .. attribute:: pid

      The process ID of the lockfile.

      :type: str

   .. attribute:: port

      The port of the lockfile.

      :type: str

   .. attribute:: password

      The password of the lockfile.

      :type: str

   .. attribute:: protocol

      The protocol of the lockfile.

      :type: str


.. py:class:: LeaguClient

   Class representing a League of Legends client.

   .. attribute:: __process_name

      The name of the League client executable file.

      :type: str

   .. attribute:: __process

      The process object representing the League client.

      :type: psutil.Process

   .. attribute:: __lockfile

      The lockfile object representing the League client's lockfile.

      :type: Lockfile

   .. py:property:: lockfile
      :type: Lockfile

      Getter method for the lockfile attribute.

      :returns: The Lockfile object representing the lockfile of the current instance.
      :rtype: Lockfile


