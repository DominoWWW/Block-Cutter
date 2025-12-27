import json

stairs = []
with open(f'tags/slabs/slabs.json') as file:
    data = json.load(file)
    stairs.extend(data["values"])

stairs.pop(0)  # Remove the first entry which is not a stair

with open(f'tags/slabs/wooden_slabs.json') as file:
    data = json.load(file)
    stairs.extend(data["values"])

for i, stair in enumerate(stairs):
    summon minecraft:item ~ ~2 ~ {Item:{id:stairs[i],count:2}}