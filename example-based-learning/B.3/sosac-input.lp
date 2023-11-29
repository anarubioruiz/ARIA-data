bot_Space(den).
bot_Space(music_room).

bot_adjacentZone(den, music_room).
bot_adjacentZone(music_room, den).

bot_containsElement(den, den_light).
bot_containsElement(den, den_occupancy).
bot_containsElement(music_room, music_room_light).
bot_containsElement(music_room, music_room_occupancy).

building_Door(d0).
bot_interfaceOf(d0, music_room).
building_Door(d2).
bot_interfaceOf(d2, music_room).
bot_interfaceOf(d2, den).

sosac_Device(den_light, smartLight).
sosac_Device(music_room_light, smartLight).
sosac_Device(den_occupancy, occupancySensor).
sosac_Device(music_room_occupancy, occupancySensor).
