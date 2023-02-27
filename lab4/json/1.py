import json
with open('sample-data.json') as f:
    data = json.load(f)

print('''=======================================================================================
DN                                                 Description           Speed    MTU" 
-------------------------------------------------- --------------------  ------  ------''')

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    print("{:<50}{:<25}{:<8}{}".format(dn, description, speed, mtu))