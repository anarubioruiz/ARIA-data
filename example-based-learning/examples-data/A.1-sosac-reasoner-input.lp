% Consider there is one room named LivingRoom. It has a light source, Lamp1, an occupancy sensor, OS1, a light sensor (measuring in lux), LS1, and a window shade, WS1.

bot_Space(living_room).

bot_containsElement(living_room, lamp1).
bot_containsElement(living_room, os1).
bot_containsElement(living_room, ls1).

building_Window(living_room_window).
bot_hasElement(living_room, living_room_window).
bot_hasSubElement(living_room_window, ws1).

sosac_Device(lamp1, smartLight).
sosac_Device(os1, occupancySensor).
sosac_Device(ls1, lightSensor).
sosac_Device(ws1, windowCover).
