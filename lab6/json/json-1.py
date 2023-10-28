import json 

with open('sample-data.json', 'r') as f:
    a=json.load(f)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------""")

for i in a["imdata"]:
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN = i["l1PhysIf"]["attributes"]["dn"], Speed = i["l1PhysIf"]["attributes"]["speed"], MTU = i["l1PhysIf"]["attributes"]["mtu"]))