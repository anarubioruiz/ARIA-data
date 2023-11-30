bot_Space(family_room).
bot_Space(kitchen_nook).

bot_adjacentZone(family_room, kitchen_nook).
bot_adjacentZone(kitchen_nook, family_room).

bot_containsElement(family_room, family_room_lamp).
bot_containsElement(family_room, family_room_sensor).
bot_containsElement(kitchen_nook, kitchen_nook_light).
bot_containsElement(kitchen_nook, kitchen_nook_sensor).

building_VirtualBoundary(vb1).
bot_interfaceOf(vb1, kitchen_nook).
bot_interfaceOf(vb1, family_room).

building_Door(d0).
bot_interfaceOf(d0, kitchen_nook).

building_Window(win1).
bot_hasElement(family_room, win1).
bot_hasSubElement(win1, family_room_curtains).

sosac_Device(family_room_lamp, smartLight).
sosac_Device(kitchen_nook_light, smartLight).
sosac_Device(family_room_sensor, occupancySensor).
sosac_Device(kitchen_nook_sensor, occupancySensor).
sosac_Device(family_room_curtains, windowCover).
