import json

with open("data.json", "r", encoding='utf-8') as file:
        # Use json.load() to read the file and parse the JSON data
        data = json.load(file)


dn = data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
descr = data["imdata"][0]["l1PhysIf"]["attributes"]["descr"]
speed = data["imdata"][0]["l1PhysIf"]["attributes"]["speed"]
mtu = data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
# print(descr)
# print(speed)
# print(mtu)
print("Interface Status")
for i in range(100):
        print("=",end='')
print("\nDN                                                   Description                 Speed        MTU")
for k in range(100):
        print("-",end='')
        if k == 50:
                print("",end=" ")
        if k == 78:
                print("",end=" ")
        if k == 89:
                print("",end=" ")

     

print("\n" + dn + "            " + descr + "                          " + speed + "       " + mtu)    
print(dn + "            " + descr + "                          " + speed + "       " + mtu)    
print(dn + "            " + descr + "                          " + speed + "       " + mtu)    