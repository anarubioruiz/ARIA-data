bot_Space(living_room).
bot_Space(kitchen).
bot_Space(studio).

bot_adjacentZone(living_room, kitchen).
bot_adjacentZone(living_room, studio).
bot_adjacentZone(kitchen, living_room).
bot_adjacentZone(kitchen, studio).
bot_adjacentZone(studio, living_room).
bot_adjacentZone(studio, kitchen).

bot_containsElement(living_room, sb1).
bot_containsElement(living_room, os1).
bot_containsElement(kitchen, main_light).
bot_containsElement(kitchen, kitchen_occupancy).
bot_containsElement(kitchen, kitchen_light_level).
bot_hasElement(kitchen, win2).
bot_containsElement(studio, studio_light).
bot_containsElement(studio, studio_occupancy).
bot_containsElement(studio, studio_light_level).
bot_hasElement(studio, win1).

building_Door(d0).
building_Door(d2).
building_Door(d1).
bot_hasSubElement(d1, door_sensor_d1).

bot_interfaceOf(d0, kitchen).
bot_interfaceOf(d1, studio).
bot_interfaceOf(d1, living_room).
bot_interfaceOf(d2, kitchen).
bot_interfaceOf(d2, living_room).

building_Window(win2).
building_Window(win1).
bot_hasSubElement(win1, studio_cover).

sosac_Device(sb1, smartLight).
sosac_Device(studio_light, smartLight).
sosac_Device(main_light, smartLight).
sosac_Device(os1, occupancySensor).
sosac_Device(studio_occupancy, occupancySensor).
sosac_Device(kitchen_occupancy, occupancySensor).
sosac_Device(studio_light_level, lightSensor).
sosac_Device(kitchen_light_level, lightSensor).
sosac_Device(studio_cover, windowCover).
