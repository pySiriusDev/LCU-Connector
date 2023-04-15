:orphan:

:py:mod:`lcu_connector.connection`
==================================

.. py:module:: lcu_connector.connection


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   lcu_connector.connection.Connection




.. py:class:: Connection

   Represents a connection object that allows for sending requests to the Riot API.

   .. attribute:: __session

      A session object for sending HTTP requests.

      :type: Session]

   .. attribute:: __riotSSL

      An SSL object for handling Riot SSL certificate.

      :type: RiotSSL

   .. attribute:: __ssl

      The path to the SSL certificate file.

      :type: Path

   .. py:property:: connected
      :type: bool

      Checks if the connection is established.

      :returns: Returns True if the connection is established, otherwise False.
      :rtype: bool

   .. py:method:: start()

      Starts a new session with the provided headers and SSL verification.



   .. py:method:: stop()

      Closes the session if it exists and sets it to None.

      :raises SessionError: If there is no active session.


   .. py:method:: get(api_url)

      Sends a GET request to the specified API URL and returns the response.

      :param api_url: The URL of the API to send the request to.
      :type api_url: str

      :returns: The response object from the GET request.
      :rtype: Response


   .. py:method:: post(api_url, data)

      Sends a POST request with the given data to the specified API URL using the active session.

      :param api_url: The URL of the API to send the request to.
      :type api_url: str
      :param data: The data to send with the POST request.
      :type data: Dict

      :returns: The response object containing the server's response to the request.
      :rtype: Response


   .. py:method:: put(api_url, data)

      Sends a PUT request with the given data to the specified API URL using the active session.

      :param api_url: The URL of the API endpoint.
      :type api_url: str
      :param data: The data to be sent in the request.
      :type data: Dict

      :returns: The response object from the request.
      :rtype: Response


   .. py:method:: delete(api_url)

      Sends a DELETE request to the specified API URL using the active session.

      :param api_url: The URL of the API endpoint to delete.
      :type api_url: str

      :returns: The response object from the DELETE request.
      :rtype: Response



