:orphan:

:py:mod:`lcu_connector`
=======================

.. py:module:: lcu_connector


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   lcu_connector.Connector




.. py:class:: Connector(start = False)

   Bases: :py:obj:`BaseConnector`, :py:obj:`lcu_connector.connection.Connection`

   Represents a connector for a Riot Games client.

   Inherits from:
       BaseConnector
       Connection

   .. attribute:: pid

      The process ID of the client.

      :type: int

   .. attribute:: url

      The URL of the client connection.

      :type: str

   .. attribute:: auth

      The authorization for the client connection.

      :type: str

   .. attribute:: headers

      The headers for the client connection.

      :type: dict


