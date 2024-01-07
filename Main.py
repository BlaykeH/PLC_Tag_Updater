from PLCCommunication import PLCCommunication
from TagReader import TagReader

plc_ip = "192.168.1.10"
tag_name = "YourTagName"

plc_comm = PLCCommunication(plc_ip)
tag_reader = TagReader(plc_comm)
tag_value = tag_reader.read_tag(tag_name)

if tag_value is not None:
    print(f"Value of {tag_name}: {tag_value}")
else:
    print(f"Failed to read {tag_name}")
