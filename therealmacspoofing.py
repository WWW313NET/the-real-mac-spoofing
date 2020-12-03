import os
import random

mac = ["83:FA:CD:A2:68:74", "DD:35:A9:39:E8:7B", "7B:E1:5B:38:67:4C", "03:07:97:E9:BE:ED", "B6:A4:AB:BE:A6:07", "FF:C7:B5:F4:48:2E", "DA:4B:BF:96:A4:49", "01:2C:4A:B7:2B:3D", "59:0E:86:23:0D:41", "6A:82:DB:B3:E1:83", "10:F9:B0:DF:25:13", "3B:FD:4E:DE:17:5E", "B1:A9:0C:A8:D0:51", "C8:FA:C5:7D:69:9A", "BA:4B:AF:4C:BD:D6", "E1:A3:88:BA:BB:9C", "50:21:18:2C:B3:35", "DA:4B:BF:96:A4:49", "83:C2:93:36:BE:7F", "FE:44:FB:7F:45:AF", "83:C2:93:36:BE:7F", "EB:72:39:1F:A9:32", "DD:35:A9:39:E8:7B", "5C:FA:5A:D0:C7:9C", "02:92:C4:2A:D1:BE"]
mac_addr = random.choice(mac)
try:
    print("what is the name of your iface?")
    iface = input(">")
    os.system("sudo ip link set dev " + iface + " down")
    os.system("sudo ip link set dev " + iface + " address " + mac_addr)
    os.system("sudo ip link set dev " + iface + " up") 
except:
    print("[+]I am changing your mac address")
    print("[-]Your mac address is not now anonymous")

print("[+]I am changing your mac address")
print("[+]Your mac address is now anonymous")