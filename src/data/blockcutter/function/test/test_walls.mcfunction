import json

walls = []
with open(f'tags/walls/walls.json') as file:
    data = json.load(file)
    walls.extend(data["values"])

for i, wall in enumerate(walls):
    summon minecraft:item ~ ~2 ~ {Item:{id:walls[i],count:4}}