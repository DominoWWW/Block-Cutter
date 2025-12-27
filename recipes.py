from beet import Context, Recipe
import json

def create_recipes(ctx: Context):
    blockcutter_stairs_recipe(ctx)
    blockcutter_slab_recipe(ctx)
    blockcutter_walls_recipe(ctx)
    blockcutter_wood_recipe(ctx)
    blockcutter_trapdoor_recipe(ctx)

    stairs_to_blocks_recipe(ctx)
    slabs_to_blocks_recipe(ctx)
    walls_to_blocks_recipe(ctx)


def blockcutter_stairs_recipe(ctx: Context):
    stairs = []
    with open(f'tags/stairs/stairs.json') as file:
        data = json.load(file)
        stairs.extend(data["values"])

    stairs.pop(0)  # Remove the first entry which is not a stair

    for i, stair in enumerate(stairs):
        stairs[i] = stair.replace("minecraft:", "")

    for stair in stairs:
        block = stair.split("_stairs")[0]
        block = block.replace("brick", "bricks")
        block = block.replace("tile", "tiles")
        block = block.replace("purpur", "purpur_block")

        print(f'{block} >> {stair}')
        ctx.data[f'minecraft:{stair}_from_{block}_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}",
            "result": {
                "id": f"minecraft:{stair}",
                "count": 1
            }
        })

    stairs = []
    with open(f'tags/stairs/wooden_stairs.json') as file:
        data = json.load(file)
        stairs.extend(data["values"])

    for stair in stairs:
        stairs[stairs.index(stair)] = stair.replace("minecraft:", "")

    for stair in stairs:
        block = stair.split("_stairs")[0]
        print(f'{block}_planks >> {stair}')
        ctx.data[f'minecraft:{stair}_from_{block}_planks_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}_planks",
            "result": {
                "id": f"minecraft:{stair}",
                "count": 1
            }
        })
def blockcutter_slab_recipe(ctx: Context):
    slabs = []
    with open(f'tags/slabs/slabs.json') as file:
        data = json.load(file)
        slabs.extend(data["values"])

    slabs.pop(0)  # Remove the first entry which is not a slab

    for i, slab in enumerate(slabs):
        slabs[i] = slab.replace("minecraft:", "")

    for slab in slabs:
        block = slab.split("_slab")[0]
        block = block.replace("brick", "bricks")
        block = block.replace("tile", "tiles")
        block = block.replace("purpur", "purpur_block")
        if block == "petrified_oak": continue

        print(f'{block} >> {slab}')
        ctx.data[f'minecraft:{slab}_from_{block}_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}",
            "result": {
                "id": f"minecraft:{slab}",
                "count": 2
            }
        })

    slabs = []
    with open(f'tags/slabs/wooden_slabs.json') as file:
        data = json.load(file)
        slabs.extend(data["values"])

    for slab in slabs:
        slabs[slabs.index(slab)] = slab.replace("minecraft:", "")

    for slab in slabs:
        block = slab.split("_slab")[0]
        print(f'{block}_planks >> {slab}')
        ctx.data[f'minecraft:{slab}_from_{block}_planks_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}_planks",
            "result": {
                "id": f"minecraft:{slab}",
                "count": 2
            }
        })
def blockcutter_walls_recipe(ctx: Context):
    walls = []
    with open(f'tags/walls/walls.json') as file:
        data = json.load(file)
        walls.extend(data["values"])

    for i, wall in enumerate(walls):
        walls[i] = wall.replace("minecraft:", "")

    for wall in walls:
        block = wall.split("_wall")[0]
        block = block.replace("brick", "bricks")
        block = block.replace("tile", "tiles")

        print(f'{block} >> {wall}')
        ctx.data[f'minecraft:{wall}_from_{block}_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}",
            "result": {
                "id": f"minecraft:{wall}",
                "count": 1
            }
        })
def blockcutter_wood_recipe(ctx: Context):
    woods = []
    with open(f'tags/slabs/wooden_slabs.json') as file:
        data = json.load(file)
        woods.extend(data["values"])

    woods.remove("minecraft:crimson_slab")
    woods.remove("minecraft:warped_slab")
    woods.remove("minecraft:bamboo_slab")

    stripped_woods = []

    for i, wood in enumerate(woods):
        woods[i] = wood.replace("minecraft:", "").replace("_slab", "")
        stripped_woods.append(wood.replace("minecraft:", "stripped_").replace("_slab", ""))

    woods.extend(stripped_woods)

    for wood in woods:
        print(f'{wood}_log >> {wood}_wood')
        ctx.data[f'minecraft:{wood}_wood_from_{wood}_log_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{wood}_log",
            "result": {
                "id": f"minecraft:{wood}_wood",
                "count": 1
            }
        })

    stems = ["crimson", "warped", "stripped_crimson", "stripped_warped"]

    for stem in stems:
        print(f'{stem}_stem >> {stem}_hyphae')
        ctx.data[f'minecraft:{stem}_wood_from_{stem}_stem_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{stem}_stem",
            "result": {
                "id": f"minecraft:{stem}_hyphae",
                "count": 1
            }
        })
def blockcutter_trapdoor_recipe(ctx: Context):
    trapdoors = []
    with open(f'tags/trapdoors/trapdoors.json') as file:
        data = json.load(file)
        trapdoors.extend(data["values"])

    trapdoors.pop(0)  # Remove the first entry which is not a slab

    for i, trapdoor in enumerate(trapdoors):
        trapdoors[i] = trapdoor.replace("minecraft:", "")

    for trapdoor in trapdoors:
        block = trapdoor.split("_trapdoor")[0]
        if (trapdoor == "iron_trapdoor"): continue
        if (block == "copper"): block = "copper_block"
        if (block == "waxed_copper"): block = "waxed_copper_block"

        print(f'{block} >> {trapdoor}')
        ctx.data[f'minecraft:{trapdoor}_from_{block}_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}",
            "result": {
                "id": f"minecraft:{trapdoor}",
                "count": 2
            }
        })

    trapdoors = []
    with open(f'tags/trapdoors/wooden_trapdoors.json') as file:
        data = json.load(file)
        trapdoors.extend(data["values"])

    for trapdoor in trapdoors:
        trapdoors[trapdoors.index(trapdoor)] = trapdoor.replace("minecraft:", "")

    for trapdoor in trapdoors:
        block = trapdoor.split("_trapdoor")[0]
        print(f'{block}_planks >> {trapdoor}')
        ctx.data[f'minecraft:{trapdoor}_from_{block}_planks_stonecutting'] = Recipe({
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{block}_planks",
            "result": {
                "id": f"minecraft:{trapdoor}",
                "count": 2
            }
        })


def stairs_to_blocks_recipe(ctx: Context):
    stairs = []
    with open(f'tags/stairs/stairs.json') as file:
        data = json.load(file)
        stairs.extend(data["values"])

    stairs.pop(0)  # Remove the first entry which is not a stair

    for i, stair in enumerate(stairs):
        stairs[i] = stair.replace("minecraft:", "")

    for stair in stairs:
        block = stair.split("_stairs")[0]
        block = block.replace("brick", "bricks")
        block = block.replace("tile", "tiles")
        block = block.replace("quartz", "quartz_block")
        block = block.replace("smooth_quartz_block", "smooth_quartz")
        block = block.replace("purpur", "purpur_block")

        print(f'{stair} >> {block}')
        ctx.data[f'minecraft:{stair}_to_{block}'] = Recipe({
            "type": "minecraft:crafting_shaped",
            "group": "stairs_to_block",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": [
                    f'minecraft:{stair}'
                ]
            },
            "result": {
                "id": f'minecraft:{block}',
                "count": 4
            },
            "show_notification": False
        })

    # Wooden stairs
    stairs = []
    with open(f'tags/stairs/wooden_stairs.json') as file:
        data = json.load(file)
        stairs.extend(data["values"])

    for stair in stairs:
        stair = stair.replace("minecraft:", "")
        block = stair.split("_stairs")[0]
        block = block.replace("brick", "bricks")

        print(f'{stair} >> {block}')
        ctx.data[f'minecraft:{stair}_to_{block}'] = Recipe({
            "type": "minecraft:crafting_shaped",
            "group": "stairs_to_block",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": [
                    f'minecraft:{stair}'
                ]
            },
            "result": {
                "id": f'minecraft:{block}_planks',
                "count": 4
            },
            "show_notification": False
        })
def slabs_to_blocks_recipe(ctx: Context):
    slabs = []
    with open(f'tags/slabs/slabs.json') as file:
        data = json.load(file)
        slabs.extend(data["values"])

    slabs.pop(0)  # Remove the first entry which is not a slab

    for i, slab in enumerate(slabs):
        slabs[i] = slab.replace("minecraft:", "")

    for slab in slabs:
        block = slab.split("_slab")[0]
        block = block.replace("brick", "bricks")
        block = block.replace("tile", "tiles")
        block = block.replace("quartz", "quartz_block")
        block = block.replace("smooth_quartz_block", "smooth_quartz")
        block = block.replace("purpur", "purpur_block")
        block = block.replace("petrified_oak", "oak_planks")

        print(f'{slab} >> {block}')
        ctx.data[f'minecraft:{slab}_to_{block}'] = Recipe({
            "type": "minecraft:crafting_shaped",
            "group": "slabs_to_block",
            "category": "building",
            "pattern": [
                "##"
            ],
            "key": {
                "#": [
                    f'minecraft:{slab}'
                ]
            },
            "result": {
                "id": f'minecraft:{block}',
                "count": 1
            },
            "show_notification": False
        })

    # Wooden slabs
    slabs = []
    with open(f'tags/slabs/wooden_slabs.json') as file:
        data = json.load(file)
        slabs.extend(data["values"])

    for slab in slabs:
        slab = slab.replace("minecraft:", "")
        block = slab.split("_slab")[0]
        block = block.replace("brick", "bricks")

        print(f'{slab} >> {block}')
        ctx.data[f'minecraft:{slab}_to_{block}'] = Recipe({
            "type": "minecraft:crafting_shaped",
            "group": "slabs_to_block",
            "category": "building",
            "pattern": [
                "##"
            ],
            "key": {
                "#": [
                    f'minecraft:{slab}'
                ]
            },
            "result": {
                "id": f'minecraft:{block}_planks',
                "count": 1
            },
            "show_notification": False
        })
def walls_to_blocks_recipe(ctx: Context):
    walls = []
    with open(f'tags/walls/walls.json') as file:
        data = json.load(file)
        walls.extend(data["values"])

    for i, wall in enumerate(walls):
        walls[i] = wall.replace("minecraft:", "")

    for wall in walls:
        block = wall.split("_wall")[0]
        block = block.replace("brick", "bricks")
        block = block.replace("tile", "tiles")
        block = block.replace("purpur", "purpur_block")
        block = block.replace("petrified_oak", "oak_planks")

        print(f'{wall} >> {block}')
        ctx.data[f'minecraft:{wall}_to_{block}'] = Recipe({
            "type": "minecraft:crafting_shaped",
            "group": "walls_to_block",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": [
                    f'minecraft:{wall}'
                ]
            },
            "result": {
                "id": f'minecraft:{block}',
                "count": 4
            },
            "show_notification": False
        })