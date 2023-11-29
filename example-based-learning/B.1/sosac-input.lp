bot_Space(meeting_room).
bot_Space(desktops).

bot_adjacentZone(meeting_room, desktops).
bot_adjacentZone(desktops, meeting_room).

bot_containsElement(meeting_room, meeting_room_light).
bot_containsElement(meeting_room, meeting_room_occupancy).
bot_containsElement(desktops, desktops_light).
bot_containsElement(desktops, desktops_occupancy).

building_Wall(wall5).
building_Door(door1).
building_Door(door2).

bot_interfaceOf(meeting_room, wall5).
bot_interfaceOf(desktops, wall5).
bot_interfaceOf(meeting_room, door1).
bot_interfaceOf(desktops, door2).

dicbm_hasConstituentSet(wall5, wall5_cs).
dicbm_hasConstituentSet(door1, door1_cs).
dicbm_hasConstituentSet(door2, door2_cs).

dicbm_ConstituentSet(wall5_cs).
dicbm_hasMaterial(wall5_cs, glass).
dicbm_ConstituentSet(door1_cs).
dicbm_hasMaterial(door1_cs, glass).
dicbm_ConstituentSet(door2_cs).
dicbm_hasMaterial(door2_cs, glass).

sosac_Device(meeting_room_light, smartLight).
sosac_Device(desktops_light, smartLight).
sosac_Device(meeting_room_occupancy, occupancySensor).
sosac_Device(desktops_occupancy, occupancySensor).
