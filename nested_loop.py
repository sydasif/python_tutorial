""" Nested loop to configure network devices"""

device_list = ["R1", "R2", "R3"]
intf_list = ["interface gig0/0", "interface gig0/1"]

for device in device_list:
    if device == "R2":
        continue
    print(f"#### Connecting to the device {device} ####\n")
    for interfac in intf_list:
        print(f"{interfac}\n description {interfac}\n")
