:orphan:

:py:mod:`lcu_connector.connector`
=================================

.. py:module:: lcu_connector.connector


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   lcu_connector.connector.BaseConnector
   lcu_connector.connector.Connector




.. py:class:: BaseConnector

   Base class that stores the attributes for the `Connector`.

   .. attribute:: __pid

      The private ID of the connector.

      :type: str

   .. attribute:: __url

      The private URL of the connector.

      :type: str

   .. attribute:: __auth

      The private authentication key of the connector.

      :type: str

   .. attribute:: __headers

      The private headers of the connector.

      :type: Dict

   .. py:property:: pid
      :type: str

      Getter for the pid attribute.

      :returns: The value of the pid attribute.
      :rtype: str

   .. py:property:: url
      :type: str

      Getter for the url attribute.

      :returns: The value of the url attribute.
      :rtype: str

   .. py:property:: auth
      :type: str

      Getter method for the auth property.

      :returns: The value of the auth property.
      :rtype: str

   .. py:property:: headers
      :type: Dict

      Getter method for the headers property.

      :returns: The value of the headers property.
      :rtype: Dict


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


