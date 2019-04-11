#1usr/bin/env python3
from napalm import get_network_driver

mydriver = get_network_driver('eos')

mydevice = mydriver('172.16.2.10', 'admin', 'alta3')

mydevice.open()

results = mydevice.compliance_report("swi_verification.yml")

print(" ---Napalm Recap--- ")
print("Version checks out - ", results.get("get_facts").get("complies"))
print("Interfaces check out - ", results.get ("get_interfaces_ip").get("complies"))
print("ICMP Complies - ", results.get("ping_SW2").get("complies"))

print("\n\n")
mydevice.close()
