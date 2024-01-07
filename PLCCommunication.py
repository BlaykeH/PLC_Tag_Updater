from pycomm3 import LogixDriver
import logging

class PLCCommunication:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.plc = None

    def connect(self):
        try:
            self.plc = LogixDriver(self.ip_address)
            self.plc.open()
            return True
        except Exception as e:
            logging.error(f"Error connecting to PLC: {e}")
            return False

    def disconnect(self):
        if self.plc:
            try:
                self.plc.close()
            except Exception as e:
                logging.error(f"Error disconnecting from PLC: {e}")


