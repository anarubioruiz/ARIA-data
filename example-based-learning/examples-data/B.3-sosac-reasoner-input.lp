% The deployment has two rooms, living_room and kitchen. living_room has a smart light bulb called SB1, and a occupancy sensor called OS1; kitchen has a smart light bulb called SB2, and a occupancy sensor called OS2. Both spaces are connected by a door.

bot_Space(living_room).
bot_Space(kitchen).

bot_adjacentSpace(living_room, kitchen).
bot_adjacentSpace(kitchen, living_room).

bot_containsElement(living_room, sb1).
bot_containsElement(living_room, os1).
bot_containsElement(kitchen, sb2).
bot_containsElement(kitchen, os2).

building_Door(door1).
bot_interfaceOf(door1, living_room).
bot_interfaceOf(door1, kitchen).

sosac_Device(sb1, smartLight).
sosac_Device(sb2, smartLight).
sosac_Device(os1, occupancySensor).
sosac_Device(os2, occupancySensor).
