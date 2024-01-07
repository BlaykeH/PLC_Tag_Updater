from PLCCommunication import PLCCommunication

class TagReader:
    def __init__(self, plc_communication):
        self.plc_communication = plc_communication

    def read_tag(self, tag_name):
        if self.plc_communication.connect():
            try:
                value = self.plc_communication.plc.read(tag_name)
                self.plc_communication.disconnect()
                return value
            except Exception as e:
                self.plc_communication.disconnect()
                print(f"Error reading tag: {e}")
                return None
        else:
            print("Connection to PLC failed.")
            return None
