import re
from unittest import mock

def create_plc_mock(plc_ip):
    plc_ip = plc_ip
    ip_address_pattern = r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    """
    Creates a mock PLC object.

    :param successful_connection: Determines if the connection should be simulated as successful or not.
    :return: A mock PLC object.
    """
    # Create a MagicMock object to represent the LogixDriver
    plc_mock = mock.MagicMock()

    # Configure the open and close methods
    if re.match(ip_address_pattern,plc_ip):
        # Simulate a successful connection
        plc_mock.open.return_value = None
        # Simulate a successful disconnection
        plc_mock.close.return_value = None
    else:
        # Simulate a connection failure by raising an exception
        plc_mock.open.side_effect = Exception("Failed to connect")
        # Simulate a disconnection failure by raising an exception
        plc_mock.close.side_effect = Exception("Failed to disconnect")

    return plc_mock
