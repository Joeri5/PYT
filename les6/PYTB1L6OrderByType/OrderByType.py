stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]

strings = []
integers = []
floats = []
booleans = []

for i in range(0, len(stuff)):
    obj = type(stuff[i])
    if obj is str:
        strings.append(stuff[i])
    elif obj is int:
        integers.append(stuff[i])
    elif obj is float:
        floats.append(stuff[i])
    elif obj is bool:
        booleans.append(stuff[i])
    else:
        print('unknown object')

print(f"Strings: {strings}")
print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Booleans: {booleans}")
